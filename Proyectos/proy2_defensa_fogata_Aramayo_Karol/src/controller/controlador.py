"""
Controlador del juego. Tiene el loop principal.

Fase: 3 - ENEMIGOS
Fase: 4 - Cola y Lista Enlazada.
Fase: 5 - Defensas con click.
Fase: 6 - Combate.
Fase: 7 - Interfaz y fin de juego.
Fase: 8 - Menú, oro y panel de defensas.
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

ANCHO = 800
ALTO = 670
TITULO = "Defensa de la Fogata"
FPS = 60


class Controlador:
    """Mantiene el juego corriendo. Une la vista y el modelo."""

    def __init__(self) -> None:
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()
        self.render = Render()

        self.mapa = Mapa()
        self.fogata = Fogata(self.mapa)

        # FASE 4
        self.cola_oleadas = Cola()
        self.activos = ListaEnlazada()
        self.temporizador = 0.0

        # FASE 5
        self.defensas = []
        self.tipo_defensa = "valla"

        # FASE 6
        self.proyectiles = []
        self.tiempo_juego = 0.0

        # FASE 7
        self.oleada = 1
        self.puntuacion = 0
        self.estado = "menu"  # menu, jugando, fin_victoria, fin_derrota
        self.fuente = pygame.font.Font(None, 28)
        self.fuente_grande = pygame.font.Font(None, 56)

        # FASE 8 - Oro inicial
        self.oro = 200

        # Fase 4 - llenar cola
        for _ in range(10):
            col = random.randint(0, self.mapa.columnas - 1)
            self.cola_oleadas.encolar(Enemigo(col=col, fila=0))

        self.run = False

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

        for _ in range(10):
            col = random.randint(0, self.mapa.columnas - 1)
            self.cola_oleadas.encolar(Enemigo(col=col, fila=0))

    def eventos(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False

            # FASE 8 - Menú de inicio
            if self.estado == "menu":
                if e.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 300 <= mouse_x <= 500 and 350 <= mouse_y <= 420:
                        self.estado = "jugando"
                return

            # FASE 8 - Fin del juego
            if self.estado in ("fin_victoria", "fin_derrota"):
                if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                    self.reiniciar()
                return

            # --- Eventos del juego ---
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    self.tipo_defensa = "valla"
                if e.key == pygame.K_2:
                    self.tipo_defensa = "torre"
                if e.key == pygame.K_3:
                    self.tipo_defensa = "muro"

            # FASE 8 - Colocar defensa con oro
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // 40
                fila = (mouse_y-70)  // 40

                if self.mapa.dentro(col, fila) and self.mapa.libre(col, fila):
                    costo = Defensa.COSTOS.get(self.tipo_defensa, 0)
                    if self.oro >= costo:
                        defensa = Defensa(col, fila, self.tipo_defensa)
                        defensa.colocar_en_mapa(self.mapa)
                        self.defensas.append(defensa)
                        self.oro -= costo

    def _actualizar(self) -> None:
        if self.estado != "jugando":
            return

        dt = self.clock.get_time() / 1000.0
        self.temporizador += dt
        self.tiempo_juego += dt

        if self.temporizador >= 1.5:
            self.temporizador = 0.0
            if not self.cola_oleadas.vacia():
                enemigo = self.cola_oleadas.desencolar()
                self.activos.insertar(enemigo)

        for enemigo in self.activos.recorrer():
            llego = enemigo.mover(dt, self.mapa)
            if llego:
                self.fogata.recibir_dano(10)
                self.activos.eliminar(enemigo)
                if not self.fogata.esta_viva():
                    self.estado = "fin_derrota"
                    return

        for defensa in self.defensas:
            if defensa.tipo == "torre" and defensa.puede_disparar(self.tiempo_juego):
                mejor_enemigo = None
                mejor_distancia = 200
                for enemigo in self.activos.recorrer():
                    dx = enemigo.x - defensa.col * 40
                    dy = (enemigo.y + 70)  - (defensa.fila * 40 + 70 ) 
                    dist = (dx ** 2 + dy ** 2) ** 0.5
                    if dist < mejor_distancia:
                        mejor_distancia = dist
                        mejor_enemigo = enemigo
                if mejor_enemigo:
                    self.proyectiles.append(Proyectil(defensa.col, defensa.fila, mejor_enemigo))

        for p in self.proyectiles[:]:
            p.mover(dt)
            if not p.activo or p.fuera_de_pantalla():
                self.proyectiles.remove(p)

        for enemigo in self.activos.recorrer():
            if not enemigo.esta_vivo():
                self.activos.eliminar(enemigo)
                self.puntuacion += 10
                self.oro += 10

        for enemigo in self.activos.recorrer():
            fila_abajo = enemigo.fila + 1
            if fila_abajo < self.mapa.filas:
                if not self.mapa.libre(enemigo.col, fila_abajo):
                    for d in self.defensas:
                        if d.col == enemigo.col and d.fila == fila_abajo:
                            d.recibir_dano(5 * dt)
                            if d.destruida():
                                self.mapa.poner(d.col, d.fila, 0)
                                self.defensas.remove(d)
                            break

        if self.cola_oleadas.vacia() and self.activos.vacia():
            self.oleada += 1
            if self.oleada > 5:
                self.estado = "fin_victoria"
            else:
                for _ in range(10 + self.oleada * 2):
                    col = random.randint(0, self.mapa.columnas - 1)
                    self.cola_oleadas.encolar(Enemigo(col=col, fila=0))

    def iniciar(self) -> None:
        self.run = True
        while self.run:
            self.eventos()
            self._actualizar()

            self.render.dibujar(
                self.pantalla,
                self.mapa,
                self.fogata,
                self.activos.recorrer(),
                self.defensas,
                self.proyectiles,
                self.oleada,
                self.puntuacion,
                self.oro,
                self.tipo_defensa,
                self.estado,
                self.fuente,
                self.fuente_grande
            )

            pygame.display.flip()
            self.clock.tick(FPS)