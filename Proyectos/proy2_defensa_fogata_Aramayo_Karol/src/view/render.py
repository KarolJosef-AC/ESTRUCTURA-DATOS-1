"""
Vista del juego. Solo dibuja, no piensa.

Fase: 2 - Grid y fogata.
"""

import pygame
from model.mapa import Mapa, TAM_CELDA, CELDA_LIBRE
from model.entidades.fogata import Fogata

FONDO = (40, 40, 40)
COLOR_LIBRE = (55, 55, 55)
COLOR_LINEA = (70, 70, 70)
COLOR_FOGATA = (220, 100, 20)
COLOR_BRASA = (255, 200, 50)
COLOR_BORDE = (255, 140, 0)
ROJO = (200, 0, 0)
VERDE = (0, 200, 0)


class Render:
    """Sabe dibujar todo lo que el juego necesita mostrar."""

    def __init__(self) -> None:
        pass

    def dibujar(self, pantalla: pygame.Surface, mapa: Mapa, fogata: Fogata) -> None:
        pantalla.fill(FONDO)
        self._grilla(pantalla, mapa)
        self._fogata(pantalla, fogata)

    def _grilla(self, pantalla: pygame.Surface, mapa: Mapa) -> None:
        for fila in range(mapa.filas):
            for col in range(mapa.columnas):
                tipo = mapa.obtener(col, fila)
                x = col * TAM_CELDA
                y = fila * TAM_CELDA
                rect = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)

                if tipo == CELDA_LIBRE:
                    pygame.draw.rect(pantalla, COLOR_LIBRE, rect)
                pygame.draw.rect(pantalla, COLOR_LINEA, rect, width=1)

    def _fogata(self, pantalla: pygame.Surface, fogata: Fogata) -> None:
        x = fogata.col * TAM_CELDA
        y = fogata.fila * TAM_CELDA
        w = fogata.ancho * TAM_CELDA
        h = fogata.alto * TAM_CELDA

        rect_cuerpo = pygame.Rect(x, y, w, h)
        pygame.draw.rect(pantalla, COLOR_FOGATA, rect_cuerpo)

        margen = 8
        rect_brasa = pygame.Rect(x + margen, y + margen, w - margen * 2, h - margen * 2)
        pygame.draw.rect(pantalla, COLOR_BRASA, rect_brasa)
        pygame.draw.rect(pantalla, COLOR_BORDE, rect_cuerpo, width=2)

        # Barra de vida
        bx = x
        by = y - 10
        bw = w
        bh = 6
        pygame.draw.rect(pantalla, ROJO, (bx, by, bw, bh))
        vida_ancho = int(bw * fogata.porcentaje_vida())
        pygame.draw.rect(pantalla, VERDE, (bx, by, vida_ancho, bh))