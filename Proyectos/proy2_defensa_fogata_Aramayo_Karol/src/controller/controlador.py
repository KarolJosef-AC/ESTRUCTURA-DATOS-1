"""
Controlador del juego. Tiene el loop principal.
Fase: 3 al 12
"""

import pygame
import random
from view.render import Render
from model.mapa import Mapa
from model.entidades.fogata import Fogata
from model.entidades.enemigo import Enemigo
from model.estructuras.cola import Cola
from model.estructuras.lista_enlazada import ListaEnlazada
from model.entidades.defensa import Defensa
from model.entidades.proyectil import Proyectil
from model.estructuras.tabla_hash import TablaHash

ANCHO = 800
ALTO = 670
TITULO = "Defensa de la Fogata"
FPS = 60


class Controlador:

    def __init__(self) -> None:
        
        #  PYGAME 
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()
        
        #  VIEW 
        self.render = Render()

        #  MODEL 
        self.mapa = Mapa()
        self.fogata = Fogata(self.mapa)

        # = ESTRUCTURAS DE DATOS MANUALES =
        self.cola_oleadas = Cola()
        self.activos = ListaEnlazada()
        self.tabla_hash = TablaHash()
        self.tabla_hash.cargar()

        #  TIEMPO 
        self.temporizador = 0.0
        self.tiempo_juego = 0.0

        #  ENTIDADES 
        self.defensas = []
        self.proyectiles = []
        self.tipo_defensa = "valla"

        #  ESTADO DEL JUEGO 
        self.oleada = 1
        self.puntuacion = 0
        self.oro = 200
        self.estado = "menu"
        self.pausa = False

        #  LOGIN 
        self.jugador = None
        self.nombre_input = ""

        #  FUENTES 
        self.fuente = pygame.font.Font(None, 28)
        self.fuente_grande = pygame.font.Font(None, 56)

        #  LLENAR COLA INICIAL 
        for _ in range(10):
            col = random.randint(0, self.mapa.columnas - 1)
            self.cola_oleadas.encolar(Enemigo(col=col, fila=0, tipo="normal"))

        self.run = False

    # PANTALLA DE LOGIN
    def login(self):
        input_activo = True
        while input_activo and self.run:
            
            #  LEER TECLAS 
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
                    return

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.nombre_input = ""
                        self.estado = "menu"
                        input_activo = False
                        return
                    
                    if e.key == pygame.K_RETURN:
                        if self.nombre_input.strip():
                            self.jugador = self.nombre_input.strip()
                            input_activo = False
                    elif e.key == pygame.K_BACKSPACE:
                        self.nombre_input = self.nombre_input[:-1]
                    else:
                        if len(self.nombre_input) < 15:
                            self.nombre_input += e.unicode

            #  DIBUJAR 
            self.render.dibujar_login(
                self.pantalla, self.nombre_input,
                self.fuente, self.fuente_grande, self.tabla_hash)

            pygame.display.flip()
            self.clock.tick(60)

    # REINICIAR
    def reiniciar(self):
        self.mapa = Mapa()
        self.fogata = Fogata(self.mapa)
        self.cola_oleadas = Cola()
        self.activos = ListaEnlazada()
        self.defensas = []
        self.proyectiles = []
        self.temporizador = 0.0
        self.tiempo_juego = 0.0
        self.oleada = 1
        self.puntuacion = 0
        self.oro = 200
        self.estado = "jugando"
        self.pausa = False
        self.tipo_defensa = "valla"

        for _ in range(10):
            col = random.randint(0, self.mapa.columnas - 1)
            self.cola_oleadas.encolar(Enemigo(col=col, fila=0, tipo="normal"))

    # EVENTOS
    def eventos(self) -> None:
        for e in pygame.event.get():
            
            if e.type == pygame.QUIT:
                self.run = False

            # MENÚ 
            if self.estado == "menu":
                if e.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 300 <= mouse_x <= 500 and 420 <= mouse_y <= 490:
                        self.estado = "login"
                return

            #  LOGIN 
            if self.estado == "login":
                return

            #  FIN DEL JUEGO 
            if self.estado == "fin_derrota":
                if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                    self.reiniciar()
                return

            #  JUEGO 
            if e.type == pygame.KEYDOWN:
                
                if e.key == pygame.K_ESCAPE:
                    self.estado = "menu"
                    return
                if e.key == pygame.K_1:
                    self.tipo_defensa = "valla"
                if e.key == pygame.K_2:
                    self.tipo_defensa = "torre"
                if e.key == pygame.K_3:
                    self.tipo_defensa = "muro"
                if e.key == pygame.K_p:
                    self.pausa = not self.pausa

            # COLOCAR DEFENSA 
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // 40
                fila = (mouse_y - 70) // 40

                if self.mapa.dentro(col, fila) and self.mapa.libre(col, fila):
                    costo = Defensa.COSTOS.get(self.tipo_defensa, 0)
                    if self.oro >= costo:
                        defensa = Defensa(col, fila, self.tipo_defensa)
                        defensa.colocar_en_mapa(self.mapa)
                        self.defensas.append(defensa)
                        self.oro -= costo

    # ACTUALIZAR 
    def _actualizar(self) -> None:
        if self.estado != "jugando" or self.pausa:
            return

        dt = self.clock.get_time() / 1000.0
        self.temporizador += dt
        self.tiempo_juego += dt

        #  Enemigos: Cola -> ListaEnlazada
        if self.temporizador >= 1.5:
            self.temporizador = 0.0
            if not self.cola_oleadas.vacia():
                enemigo = self.cola_oleadas.desencolar()
                self.activos.insertar(enemigo)

        #  MOVER ENEMIGOS 
        for enemigo in self.activos.recorrer():
            llego = enemigo.mover(dt, self.mapa)
            if llego:
                self.fogata.recibir_dano(10)
                self.activos.eliminar(enemigo)

                if not self.fogata.esta_viva():
                    self.estado = "fin_derrota"
                    self.tabla_hash.insertar(self.jugador, self.puntuacion)
                    self.tabla_hash.guardar()
                    return

        #  TORRES DISPARAN 
        for defensa in self.defensas:
            if defensa.tipo == "torre" and defensa.puede_disparar(self.tiempo_juego):
                mejor_enemigo = None
                mejor_distancia = 200
                for enemigo in self.activos.recorrer():
                    dx = enemigo.x - defensa.col * 40
                    dy = enemigo.y - defensa.fila * 40
                    dist = (dx ** 2 + dy ** 2) ** 0.5
                    if dist < mejor_distancia:
                        mejor_distancia = dist
                        mejor_enemigo = enemigo
                if mejor_enemigo:
                    self.proyectiles.append(Proyectil(defensa.col, defensa.fila, mejor_enemigo))

        #  MOVER PROYECTILES 
        for p in self.proyectiles[:]:
            p.mover(dt)
            if not p.activo or p.fuera_de_pantalla():
                self.proyectiles.remove(p)

        #  ELIMINAR ENEMIGOS MUERTOS 
        for enemigo in self.activos.recorrer():
            if not enemigo.esta_vivo():
                self.activos.eliminar(enemigo)
                self.puntuacion += 10
                self.oro += 10

        #  ENEMIGOS ATACAN DEFENSAS 
        for enemigo in self.activos.recorrer():
            fila_abajo = enemigo.fila + 1
            if fila_abajo < self.mapa.filas:
                if not self.mapa.libre(enemigo.col, fila_abajo):
                    for d in self.defensas:
                        if d.col == enemigo.col and d.fila == fila_abajo:
                            dano = 15 if enemigo.tipo == "tanque" else 5
                            d.recibir_dano(dano * dt)
                            if d.destruida():
                                self.mapa.poner(d.col, d.fila, 0)
                                self.defensas.remove(d)
                            break

        #  NUEVA OLEADA 
        if self.cola_oleadas.vacia() and self.activos.vacia():
            self.oleada += 1
            cantidad = 10 + self.oleada * 2
            for _ in range(cantidad):
                col = random.randint(0, self.mapa.columnas - 1)
                tipo = random.choice(["normal", "normal", "tanque"])
                self.cola_oleadas.encolar(Enemigo(col=col, fila=0, tipo=tipo))

    # GAME LOOP PRINCIPAL
    def iniciar(self) -> None:
        self.run = True
        while self.run:
            
            #  MENÚ 
            while self.run and self.estado == "menu":
                self.eventos()
                self.render.dibujar(
                    self.pantalla, self.mapa, self.fogata,
                    [], [], [], 0, 0, 0, "valla", "", "menu",
                    self.fuente, self.fuente_grande, self.tabla_hash)
                pygame.display.flip()
                self.clock.tick(FPS)

                if self.estado == "login":
                    self.nombre_input = ""
                    self.jugador = None
                    self.pausa = False
                    self.login()
                    if self.jugador:
                        self.estado = "jugando"
                    else:
                        self.estado = "menu"

            #  JUEGO 
            while self.run and self.estado == "jugando":
                self.eventos()
                self._actualizar()
                self.render.dibujar(
                    self.pantalla, self.mapa, self.fogata,
                    self.activos.recorrer(), self.defensas, self.proyectiles,
                    self.oleada, self.puntuacion, self.oro,
                    self.tipo_defensa, self.jugador if self.jugador else "",
                    self.estado, self.fuente, self.fuente_grande,
                    self.tabla_hash, self.pausa)
                pygame.display.flip()
                self.clock.tick(FPS)

                if self.estado == "menu":
                    self.reiniciar()
                    self.estado = "menu"

            #  FIN DEL JUEGO 
            while self.run and self.estado == "fin_derrota":
                self.eventos()
                self.render.dibujar(
                    self.pantalla, self.mapa, self.fogata,
                    self.activos.recorrer(), self.defensas, self.proyectiles,
                    self.oleada, self.puntuacion, self.oro,
                    self.tipo_defensa, self.jugador if self.jugador else "",
                    self.estado, self.fuente, self.fuente_grande,
                    self.tabla_hash, self.pausa)
                pygame.display.flip()
                self.clock.tick(FPS)

                if self.estado == "jugando":
                    self.estado = "fin_derrota"
                elif self.estado == "menu":
                    break

            #  LOGIN 
            while self.run and self.estado == "login":
                self.nombre_input = ""
                self.jugador = None
                self.login()
                if self.jugador:
                    self.reiniciar()
                    self.estado = "jugando"
                else:
                    self.estado = "menu"