"""
Controlador del juego. Tiene el loop principal.

Fase: 2 - Grid y fogata.
"""

import pygame
from view.render import Render
from model.mapa import Mapa
from model.entidades.fogata import Fogata

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

        self.run = False

    def eventos(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False

    def _actualizar(self) -> None:
        pass

    def iniciar(self) -> None:
        self.run = True
        while self.run:
            self.eventos()
            self._actualizar()
            self.render.dibujar(self.pantalla, self.mapa, self.fogata)
            pygame.display.flip()
            self.clock.tick(FPS)