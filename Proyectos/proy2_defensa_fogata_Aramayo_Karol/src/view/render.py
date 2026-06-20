"""
Vista del juego. Solo dibuja, no piensa.

Fase: 8 - Menú, panel de defensas con oro.
"""

import pygame
from model.mapa import Mapa, TAM_CELDA, CELDA_LIBRE
from model.entidades.fogata import Fogata
from model.entidades.defensa import Defensa

FONDO = (40, 40, 40)
COLOR_LIBRE = (55, 55, 55)
COLOR_LINEA = (70, 70, 70)
COLOR_FOGATA = (220, 100, 20)
COLOR_BRASA = (255, 200, 50)
COLOR_BORDE = (255, 140, 0)
ROJO = (200, 0, 0)
VERDE = (0, 200, 0)
ENEMIGO_COLOR = (180, 40, 40)


class Render:
    """Sabe dibujar todo lo que el juego necesita mostrar."""

    def __init__(self) -> None:
        pass

    def dibujar(self, pantalla, mapa, fogata, enemigos, defensas, proyectiles,
                oleada, puntuacion, oro, tipo_defensa, estado, fuente, fuente_grande):
        pantalla.fill(FONDO)

        if estado == "menu":
            self._pantalla_menu(pantalla, fuente_grande)
            return

        self._grilla(pantalla, mapa)
        self._fogata(pantalla, fogata)
        self._enemigos(pantalla, enemigos)
        self._defensas(pantalla, defensas)
        self._proyectiles(pantalla, proyectiles)
        self._ui(pantalla, oleada, puntuacion, oro, tipo_defensa, fuente)

        if estado in ("fin_victoria", "fin_derrota"):
            victoria = (estado == "fin_victoria")
            self._pantalla_final(pantalla, victoria, fuente_grande)

    def _grilla(self, pantalla, mapa):
        for fila in range(mapa.filas):
            for col in range(mapa.columnas):
                tipo = mapa.obtener(col, fila)
                x = col * TAM_CELDA
                y = fila * TAM_CELDA + 70
                rect = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)
                if tipo == CELDA_LIBRE:
                    pygame.draw.rect(pantalla, COLOR_LIBRE, rect)
                pygame.draw.rect(pantalla, COLOR_LINEA, rect, width=1)

    def _fogata(self, pantalla, fogata):
        x = fogata.col * TAM_CELDA
        y = fogata.fila * TAM_CELDA +70

        w = fogata.ancho * TAM_CELDA
        h = fogata.alto * TAM_CELDA
        rect_cuerpo = pygame.Rect(x, y, w, h)
        pygame.draw.rect(pantalla, COLOR_FOGATA, rect_cuerpo)
        margen = 8
        rect_brasa = pygame.Rect(x + margen, y + margen, w - margen * 2, h - margen * 2)
        pygame.draw.rect(pantalla, COLOR_BRASA, rect_brasa)
        pygame.draw.rect(pantalla, COLOR_BORDE, rect_cuerpo, width=2)
        bx = x
        by = y - 10
        bw = w
        bh = 6
        pygame.draw.rect(pantalla, ROJO, (bx, by, bw, bh))
        vida_ancho = int(bw * fogata.porcentaje_vida())
        pygame.draw.rect(pantalla, VERDE, (bx, by, vida_ancho, bh))

    def _enemigos(self, pantalla, enemigos):
        for enemigo in enemigos:
            x = enemigo.col * TAM_CELDA
            y = int(enemigo.y) + 70

            w = TAM_CELDA
            h = TAM_CELDA
            rect = pygame.Rect(x, y, w, h)
            pygame.draw.rect(pantalla, ENEMIGO_COLOR, rect)
            bx = x
            by = y - 6
            bw = w
            bh = 4
            pygame.draw.rect(pantalla, ROJO, (bx, by, bw, bh))
            vida_w = int(bw * enemigo.porcentaje_vida())
            pygame.draw.rect(pantalla, VERDE, (bx, by, vida_w, bh))

    def _defensas(self, pantalla, defensas):
        for d in defensas:
            x = d.col * TAM_CELDA
            y = d.fila * TAM_CELDA + 70

            rect = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)
            pygame.draw.rect(pantalla, d.color, rect)
            pygame.draw.rect(pantalla, (0, 0, 0), rect, 2)

    def _proyectiles(self, pantalla, proyectiles):
        for p in proyectiles:
            pygame.draw.circle(pantalla, (255, 255, 0), (int(p.x), int(p.y)), 4)

    def _ui(self, pantalla, oleada, puntuacion, oro, tipo_defensa, fuente):
        """Panel superior con oleada, puntos, oro y defensas disponibles."""
        # Panel más alto (70 píxeles)
        panel = pygame.Rect(0, 0, 800, 70)
        pygame.draw.rect(pantalla, (15, 15, 25), panel)
        pygame.draw.line(pantalla, (60, 60, 80), (0, 70), (800, 70), 1)

        # Textos arriba
        texto_oleada = fuente.render(f"Oleada: {oleada}", True, (255, 255, 255))
        texto_puntos = fuente.render(f"Pts: {puntuacion}", True, (255, 255, 255))
        texto_oro = fuente.render(f"Oro: {oro}", True, (255, 215, 0))
        pantalla.blit(texto_oleada, (10, 8))
        pantalla.blit(texto_puntos, (160, 8))
        pantalla.blit(texto_oro, (300, 8))

        # Defensas (más abajo, dentro del panel)
        opciones = [
            ("Valla", (139, 90, 43), 490, Defensa.COSTOS["valla"]),
            ("Torre", (100, 100, 150), 590, Defensa.COSTOS["torre"]),
            ("Muro", (80, 80, 80), 690, Defensa.COSTOS["muro"]),
        ]
        for nombre, color, x, costo in opciones:
            rect = pygame.Rect(x, 12, 36, 36)
            pygame.draw.rect(pantalla, color, rect)
            if nombre.lower() == tipo_defensa:
                pygame.draw.rect(pantalla, (255, 255, 255), rect, 3)
            else:
                pygame.draw.rect(pantalla, (100, 100, 100), rect, 1)
            texto_nombre = fuente.render(f"{nombre} ${costo}", True, (200, 200, 200))
            pantalla.blit(texto_nombre, (x, 50))

    def _pantalla_menu(self, pantalla, fuente_grande):
        titulo = fuente_grande.render("DEFENSA DE LA FOGATA", True, (255, 200, 50))
        titulo_rect = titulo.get_rect(center=(400, 150))
        pantalla.blit(titulo, titulo_rect)
        boton = pygame.Rect(300, 350, 200, 70)
        pygame.draw.rect(pantalla, (0, 150, 0), boton, border_radius=15)
        texto_jugar = fuente_grande.render("JUGAR", True, (255, 255, 255))
        texto_jugar_rect = texto_jugar.get_rect(center=boton.center)
        pantalla.blit(texto_jugar, texto_jugar_rect)

    def _pantalla_final(self, pantalla, victoria, fuente_grande):
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
        texto_r = fuente_grande.render("Presiona R para reiniciar", True, (255, 255, 255))
        texto_r_rect = texto_r.get_rect(center=(400, 330))
        pantalla.blit(texto_r, texto_r_rect)

    def _proyectiles(self, pantalla, proyectiles):
        for p in proyectiles:
            pygame.draw.circle(pantalla, (255, 255, 0), (int(p.x), int(p.y) + 70), 4)