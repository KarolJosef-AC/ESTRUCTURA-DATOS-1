"""
Vista del juego. Solo dibuja, no piensa.

Fase: 2 - ENEMIGOS
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
# FASE 3 - ENEMIGOS
ENEMIGO_COLOR = (180, 40, 40)
#


class Render:
    """Sabe dibujar todo lo que el juego necesita mostrar."""

    def __init__(self) -> None:
        pass
## FASE 7 - Nuevos parámetros de UI
    def dibujar(self, pantalla, mapa, fogata, enemigos, defensas, proyectiles,
                oleada, puntuacion, juego_terminado, victoria, fuente, fuente_grande):
    ## FIN FASE 7
        pantalla.fill(FONDO)
        self._grilla(pantalla, mapa)
        self._fogata(pantalla, fogata)
        self._enemigos(pantalla, enemigos)
        self._defensas(pantalla, defensas)
        self._proyectiles(pantalla, proyectiles)
        ## FASE 7 - Dibujar UI y pantalla final
        self._ui(pantalla, oleada, puntuacion, fuente)
        if juego_terminado:
            self._pantalla_final(pantalla, victoria, fuente_grande)
        ## FIN FASE 7
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

    # FASE 3 - ENEMIGOS
    def _enemigos(self, pantalla: pygame.Surface, enemigos:list) -> None:
        """Dibuja cada enemigo y su barra de vida."""
        for enemigo in enemigos:
            x = enemigo.col * TAM_CELDA
            y = int(enemigo.y)
            w = TAM_CELDA
            h = TAM_CELDA
            rect = pygame.Rect(x, y, w, h)
            pygame.draw.rect(pantalla, ENEMIGO_COLOR, rect)

            # barra de vida
            bx = x
            by = y - 6
            bw = w
            bh = 4
            pygame.draw.rect(pantalla, ROJO, (bx, by, bw, bh))
            vida_w = int(bw * enemigo.porcentaje_vida())
            pygame.draw.rect(pantalla, VERDE, (bx, by, vida_w, bh))
    
    def _defensas(self, pantalla:pygame.surface, defensas:list) -> None:
        """Dibuja cada defensa en su celda"""

        for d in defensas:
            x = d.col * TAM_CELDA
            y = d.fila * TAM_CELDA
            rect = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)
            pygame.draw.rect(pantalla, d.color, rect)
            pygame.draw.rect(pantalla, (0, 0, 0), rect, 2)

    # FASE 6 - DIBUJAR PROYEC
    def _proyectiles(self, pantalla, proyectiles):
        """ Dibuja cada proyectil como un punto amarillo."""
        for p in proyectiles:
            pygame.draw.circle(pantalla, (255, 255, 0), (int(p.x), int(p.y)), 4)
    # FIN


    ## FASE 7 - Interfaz de usuario
    def _ui(self, pantalla, oleada, puntuacion, fuente):
        """Muestra oleada y puntuacion en la parte superior."""
        texto_oleada = fuente.render(f"Oleada: {oleada}", True, (255, 255, 255))
        texto_puntos = fuente.render(f"Puntos: {puntuacion}", True, (255, 255, 255))
        pantalla.blit(texto_oleada, (10, 5))
        pantalla.blit(texto_puntos, (10, 30))

    def _pantalla_final(self, pantalla, victoria, fuente_grande):
        """Muestra pantalla de victoria o derrota."""
        # Fondo semitransparente
        overlay = pygame.Surface((800, 600))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))

        if victoria:
            texto = fuente_grande.render("¡VICTORIA!", True, (0, 255, 0))
        else:
            texto = fuente_grande.render("GAME OVER", True, (255, 0, 0))

        texto_rect = texto.get_rect(center=(400, 250))
        pantalla.blit(texto, texto_rect)

        # Instrucción para reiniciar
        texto_r = fuente_grande.render("Presiona R para reiniciar", True, (255, 255, 255))
        texto_r_rect = texto_r.get_rect(center=(400, 330))
        pantalla.blit(texto_r, texto_r_rect)
    ## FIN FASE 7