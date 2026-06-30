"""
Controlador del juego. Tiene el loop principal.
=================================================
Fase: 12 - Panel planificador.

Dirige el juego: recibe input del usuario, registra acciones
en el planificador, y coordina Modelo y Vista.

Arquitectura MVC:
    MODELO: Entidades, estructuras de datos, lógica del juego.
    VISTA: Renderizado en pantalla.
    CONTROLADOR: controla y game loop.

Constantes de ventana:
    ANCHO_MAPA  = 800   (20 celdas * 40px)
    ANCHO_PANEL = 200   (panel del planificador)
    ANCHO       = 1000  (total)
    ALTO        = 670
    ALTO_HUD    = 70
"""

import pygame
import random
from view.render import Render
from model.mapa import Mapa, TAM_CELDA
from model.entidades.fogata import Fogata
from model.entidades.enemigo import Enemigo
from model.estructuras.cola import Cola
from model.estructuras.lista_enlazada import ListaEnlazada
from model.entidades.defensa import Defensa
from model.estructuras.tabla_hash import TablaHash
from model.estructuras.planificador import PlanificadorAcciones
from model.logica_juego import LogicaJuego

ANCHO_MAPA  = 800
ANCHO_PANEL = 200
ANCHO       = ANCHO_MAPA + ANCHO_PANEL
ALTO        = 670
ALTO_HUD    = 70
TITULO      = "Defensa de la Fogata"
FPS         = 60


class Controlador:
    """
    Controlador principal del juego.

    controla el game loop, gestiona el input del usuario,
    registra acciones en el planificador y coordina Modelo-Vista.
    """

    def __init__(self) -> None:
        """Inicializa pygame, estructuras de datos y estado del juego."""
        
        #  PYGAME 
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()

        #  VISTA (View) 
        self.render = Render()

        #  MODELO (Model) 
        self.mapa   = Mapa()
        self.fogata = Fogata(self.mapa)

        #  ESTRUCTURAS DE DATOS 
        self.cola_oleadas = Cola()
        self.activos      = ListaEnlazada()
        self.tabla_hash   = TablaHash()
        self.tabla_hash.cargar()
        self.planificador = PlanificadorAcciones()
        self.logica       = LogicaJuego(self)

        #  TIEMPO 
        self.temporizador = 0.0
        self.tiempo_juego = 0.0

        #  ENTIDADES EN JUEGO 
        self.defensas    = []
        self.proyectiles = []
        self.tipo_defensa = "valla"

        #  ESTADO DEL JUEGO 
        self.oleada      = 1
        self.puntuacion  = 0
        self.oro         = 200
        self.estado      = "menu"
        self.pausa       = False

        #  JUGADOR 
        self.jugador      = None
        self.nombre_input = ""

        #  FUENTES 
        self.fuente       = pygame.font.Font(None, 28)
        self.fuente_grande = pygame.font.Font(None, 56)

        #  INICIALIZACIÓN FINAL 
        self._generar_oleada_inicial()
        self.run = False

    #  Inicialización 

    def _generar_oleada_inicial(self) -> None:
        """Llena la cola con 10 enemigos normales iniciales."""
        for _ in range(10):
            col = random.randint(0, self.mapa.columnas - 1)
            self.cola_oleadas.encolar(Enemigo(col=col, fila=0, tipo="normal"))

    #  Login ─

    def login(self) -> None:
        """
        Pantalla de ingreso de nombre.
        Captura teclado hasta ENTER o ESC.
        """
        input_activo = True
        while input_activo and self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
                    return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.nombre_input = ""
                        self.estado = "menu"
                        return
                    elif e.key == pygame.K_RETURN:
                        if self.nombre_input.strip():
                            self.jugador = self.nombre_input.strip()
                            input_activo = False
                    elif e.key == pygame.K_BACKSPACE:
                        self.nombre_input = self.nombre_input[:-1]
                    else:
                        if len(self.nombre_input) < 15:
                            self.nombre_input += e.unicode

            self.render.dibujar_login(
                self.pantalla, self.nombre_input,
                self.fuente, self.fuente_grande, self.tabla_hash)
            
            pygame.display.flip()
            self.clock.tick(FPS)

    #  Reinicio 

    def reiniciar(self) -> None:
        """Reinicia todo el estado para una nueva partida."""
        self.mapa        = Mapa()
        self.fogata      = Fogata(self.mapa)
        self.cola_oleadas = Cola()
        self.activos     = ListaEnlazada()
        self.defensas    = []
        self.proyectiles = []
        self.temporizador = 0.0
        self.tiempo_juego = 0.0
        self.oleada      = 1
        self.puntuacion  = 0
        self.oro         = 200
        self.estado      = "jugando"
        self.pausa       = False
        self.tipo_defensa = "valla"
        self._generar_oleada_inicial()

    #  Eventos ─

    def eventos(self) -> None:
        """
        Procesa eventos de teclado y ratón.
        Maneja menú, colocación de defensas y pausa.
        """
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False

            if self.estado == "menu":
                if e.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if 400 <= mx <= 600 and 420 <= my <= 478:
                        self.estado = "login"
                return

            if self.estado in ("login", "fin_derrota"):
                if self.estado == "fin_derrota":
                    if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                        self.reiniciar()
                return

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

            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx >= ANCHO_MAPA:
                    continue
                col  = mx // TAM_CELDA
                fila = (my - ALTO_HUD) // TAM_CELDA
                if self.mapa.dentro(col, fila) and self.mapa.libre(col, fila):
                    costo = Defensa.COSTOS.get(self.tipo_defensa, 0)
                    if self.oro >= costo:
                        defensa = Defensa(col, fila, self.tipo_defensa)
                        defensa.colocar_en_mapa(self.mapa)
                        self.defensas.append(defensa)
                        self.oro -= costo

    #  Tick principal 

    def _actualizar(self) -> None:
        """
        Tick del juego. Registra todas las acciones en el planificador
        y las ejecuta en orden de prioridad.

        Prioridades:
            0 CRITICO  - Verificar llegada a fogata
            1 ALTO     - Torres disparan
            2 NORMAL   - Spawnear enemigo, mover proyectiles, verificar oleada
            3 BAJO     - Limpiar muertos, ataques a defensas
        """
        #  Solo ejecutar si está jugando y no pausado 
        if self.estado != "jugando" or self.pausa:
            return

        #  Calcular tiempo transcurrido 
        dt = self.clock.get_time() / 1000.0
        self.temporizador += dt
        self.tiempo_juego += dt

        L = self.logica

        #  REGISTRAR ACCIONES EN EL PLANIFICADOR 

        #  PRIORIDAD 0 (CRÍTICO): Verificar si cada enemigo llegó a la fogata 
        for enemigo in self.activos.recorrer():
            self.planificador.registrar( 0, f"llegada_{enemigo.tipo}",
                                        lambda e=enemigo: L.verificar_llegada(e, dt))

        #  PRIORIDAD 1 (ALTO): Cada torre busca objetivo y dispara 
        for defensa in self.defensas:
            if defensa.tipo == "torre":
                self.planificador.registrar(1, f"torre_{defensa.col},{defensa.fila}",
                                        lambda d=defensa: L.disparar_torre(d))

        #  PRIORIDAD 2 (NORMAL): Sacar enemigo de la cola cada 1.5s 
        if self.temporizador >= 1.5:
            self.temporizador = 0.0
            self.planificador.registrar(2, "spawnear_enemigo",
                                        lambda: L.spawnear_enemigo())

        #  PRIORIDAD 2 (NORMAL): Mover todos los proyectiles en vuelo 
        self.planificador.registrar(2, "proyectiles",
                                    lambda: L.mover_proyectiles(dt))

        #  PRIORIDAD 2 (NORMAL): Verificar si toca generar nueva oleada 
        self.planificador.registrar(2, "verificar_oleada",
                                    lambda: L.verificar_nueva_oleada())

        #  PRIORIDAD 3 (BAJO): Eliminar enemigos muertos y atacar defensas 
        self.planificador.registrar(3, "limpieza",
                                    lambda: L.limpiar_y_atacar(dt))

        # ═══════════════════════════════════════════════════════════════════

        #  Actualizar panel del planificador cada 60 frames 
        if self.planificador._contador % 60 == 0:
            self.render.actualizar_historial(list(self.planificador._acciones))

        #  EJECUTAR TODO EN ORDEN DE PRIORIDAD (0 → 1 → 2 → 3) 
        self.planificador.ejecutar_frame()

    #  Game loop ─

    def iniciar(self) -> None:
        """Game loop principal. Despacha según el estado del juego."""
        self.run = True
        while self.run:

            # MENÚ
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
                        self.reiniciar()
                        self.estado = "jugando"
                    else:
                        self.estado = "menu"

            # JUEGO
            while self.run and self.estado == "jugando":
                self.eventos()
                self._actualizar()
                self.render.dibujar(
                    self.pantalla, self.mapa, self.fogata,
                    self.activos.recorrer(), self.defensas, self.proyectiles,
                    self.oleada, self.puntuacion, self.oro,
                    self.tipo_defensa,
                    self.jugador if self.jugador else "",
                    self.estado, self.fuente, self.fuente_grande,
                    self.tabla_hash, self.pausa)
                pygame.display.flip()
                self.clock.tick(FPS)

                if self.estado == "menu":
                    self.reiniciar()
                    self.estado = "menu"

            # FIN DEL JUEGO
            while self.run and self.estado == "fin_derrota":
                self.eventos()
                self.render.dibujar(
                    self.pantalla, self.mapa, self.fogata,
                    self.activos.recorrer(), self.defensas, self.proyectiles,
                    self.oleada, self.puntuacion, self.oro,
                    self.tipo_defensa,
                    self.jugador if self.jugador else "",
                    self.estado, self.fuente, self.fuente_grande,
                    self.tabla_hash, self.pausa)
                pygame.display.flip()
                self.clock.tick(FPS)

                if self.estado == "jugando":
                    self.reiniciar()
                elif self.estado == "menu":
                    break

            # LOGIN directo
            while self.run and self.estado == "login":
                self.nombre_input = ""
                self.jugador = None
                self.login()
                if self.jugador:
                    self.reiniciar()
                    self.estado = "jugando"
                else:
                    self.estado = "menu"