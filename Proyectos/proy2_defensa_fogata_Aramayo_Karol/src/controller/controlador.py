"""
Controlador del juego. Tiene el loop principal.

Fase: 3 - ENEMIGOS
Fase: 4 - Cola y Lista Enlazada.
Fase: 5 - Defensas con click.
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

ANCHO = 800
ALTO = 600
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

        # FASE 4 - enemigos en estructuras
        self.cola_oleadas = Cola()
        self.activos = ListaEnlazada()
        self.temporizador = 0.0

        # FASE 5 - lista defensas y tipo
        self.defensas = []
        self.tipo_defensa = "valla"

        # Fase 4 - llenar enemigos en la cola
        for _ in range(10):
            col = random.randint(0, self.mapa.columnas - 1)
            self.cola_oleadas.encolar(Enemigo(col=col, fila=0))

        self.run = False

    def eventos(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False

            # FASE 5 - cambiar tipo de defensa con teclas
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    self.tipo_defensa = "valla"
                if e.key == pygame.K_2:
                    self.tipo_defensa = "torre"
                if e.key == pygame.K_3:
                    self.tipo_defensa = "muro"

            # FASE 5 - colocar defensa con click
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // 40
                fila = mouse_y // 40

                if self.mapa.dentro(col, fila) and self.mapa.libre(col, fila):
                    defensa = Defensa(col, fila, self.tipo_defensa)
                    defensa.colocar_en_mapa(self.mapa)
                    self.defensas.append(defensa)

    def _actualizar(self) -> None:
        dt = self.clock.get_time() / 1000.0
        self.temporizador += dt

        # Fase 4 - enemigos de la cola a lista enlazada
        if self.temporizador >= 1.5:
            self.temporizador = 0.0
            if not self.cola_oleadas.vacia():
                enemigo = self.cola_oleadas.desencolar()
                self.activos.insertar(enemigo)

        # Fase 4 - recorrer lista enlazada
        for enemigo in self.activos.recorrer():
            llego = enemigo.mover(dt, self.mapa)
            if llego:
                self.fogata.recibir_dano(10)
                self.activos.eliminar(enemigo)

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
                self.defensas
            )

            pygame.display.flip()
            self.clock.tick(FPS)