"""
Controlador del juego. Tiene el loop principal.

Fase: 3 - ENEMIGOS
"""

import pygame
import random # fase 3
from view.render import Render
from model.mapa import Mapa
from model.entidades.fogata import Fogata
from model.entidades.enemigo import Enemigo


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
        
        # FASE 3 - enemigos 
        self.enemigos = []
        self.temporizador = 0.0
        #

        self.run = False

    def eventos(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False

    def _actualizar(self) -> None:
        # Fase 3
        dt = self.clock.get_time() / 1000.0
        self.temporizador += dt

        # crea enemigos cada 1.5 segundos de una columna aleatoria
        if self.temporizador >= 1.5:
            self.temporizador = 0.0
            col = random.randint(0, self.mapa.columnas - 1)
            self.enemigos.append(Enemigo(col=col, fila = 0))
        # mover enemigos y ver si llegan a la fogata
        for enemigo in self.enemigos[:]:
            llego = enemigo.mover(dt, self.mapa)
            if llego:
                self.fogata.recibir_dano(10)
                self.enemigos.remove(enemigo)


    def iniciar(self) -> None:
        self.run = True
        while self.run:
            self.eventos()
            self._actualizar()
            self.render.dibujar(self.pantalla, self.mapa, self.fogata, self.enemigos)
            pygame.display.flip()
            self.clock.tick(FPS)