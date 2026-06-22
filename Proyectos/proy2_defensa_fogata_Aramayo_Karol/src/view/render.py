"""
Vista del juego. Solo dibuja, no piensa.

Fase: 11 - Mejora visual de entidades.
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
                oleada, puntuacion, oro, tipo_defensa, jugador, estado, fuente, 
                fuente_grande, tabla_hash = None, pausa = False):
        pantalla.fill(FONDO)

        if estado == "menu":
            self._pantalla_menu(pantalla, fuente_grande, fuente, tabla_hash)
            return

        self._grilla(pantalla, mapa)
        self._fogata(pantalla, fogata)
        self._enemigos(pantalla, enemigos)
        self._defensas(pantalla, defensas)
        self._proyectiles(pantalla, proyectiles)
        self._ui(pantalla, oleada, puntuacion, oro, tipo_defensa, jugador, fuente)
        if estado == "jugando" and pausa:
            self._pantalla_pausa(pantalla, fuente_grande)

        if estado == "fin_derrota":
            self._pantalla_final(pantalla, False, jugador, puntuacion, fuente_grande, fuente)

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
        y = fogata.fila * TAM_CELDA + 70
        w = fogata.ancho * TAM_CELDA
        h = fogata.alto * TAM_CELDA

        base = pygame.Rect(x + 5, y + h - 15, w - 10, 15)
        pygame.draw.rect(pantalla, (101, 67, 33), base)
        pygame.draw.rect(pantalla, (80, 50, 20), base, 2)

        cx = x + w // 2
        cy = y + h // 2 - 5
        pygame.draw.circle(pantalla, (255, 100, 0), (cx, cy), 22)
        pygame.draw.circle(pantalla, (255, 180, 0), (cx - 3, cy - 5), 16)
        pygame.draw.circle(pantalla, (255, 255, 100), (cx + 2, cy - 10), 8)

        bx = x
        by = y - 14
        bw = w
        bh = 8
        pygame.draw.rect(pantalla, ROJO, (bx, by, bw, bh))
        vida_ancho = int(bw * fogata.porcentaje_vida())
        pygame.draw.rect(pantalla, VERDE, (bx, by, vida_ancho, bh))

    def _enemigos(self, pantalla, enemigos):
        for enemigo in enemigos:
            x = enemigo.col * TAM_CELDA + TAM_CELDA // 2
            y = int(enemigo.y) + 70 + TAM_CELDA // 2

            if enemigo.tipo == "normal":
                pygame.draw.circle(pantalla, enemigo.color, (x, y), 16)
                pygame.draw.circle(pantalla, (255, 255, 255), (x - 5, y - 4), 5)
                pygame.draw.circle(pantalla, (255, 255, 255), (x + 5, y - 4), 5)
                pygame.draw.circle(pantalla, (0, 0, 0), (x - 5, y - 4), 2)
                pygame.draw.circle(pantalla, (0, 0, 0), (x + 5, y - 4), 2)
            elif enemigo.tipo == "tanque":
                rect = pygame.Rect(x - 16, y - 16, 32, 32)
                pygame.draw.rect(pantalla, enemigo.color, rect, border_radius=6)
                pygame.draw.circle(pantalla, (255, 255, 0), (x - 6, y - 5), 4)
                pygame.draw.circle(pantalla, (255, 255, 0), (x + 6, y - 5), 4)

            bx = x - 16
            by = y - 24
            bw = 32
            bh = 5
            pygame.draw.rect(pantalla, ROJO, (bx, by, bw, bh))
            vida_w = int(bw * enemigo.porcentaje_vida())
            pygame.draw.rect(pantalla, VERDE, (bx, by, vida_w, bh))

    def _defensas(self, pantalla, defensas):
        for d in defensas:
            x = d.col * TAM_CELDA
            y = d.fila * TAM_CELDA + 70

            if d.tipo == "valla":
                for i in range(4):
                    px = x + 5 + i * 10
                    pygame.draw.line(pantalla, d.color, (px, y + 5), (px, y + 35), 3)
                pygame.draw.line(pantalla, d.color, (x + 2, y + 12), (x + 38, y + 12), 3)
                pygame.draw.line(pantalla, d.color, (x + 2, y + 28), (x + 38, y + 28), 3)

            elif d.tipo == "torre":
                cx = x + 20
                cy = y + 20
                pygame.draw.circle(pantalla, (101, 67, 33), (cx, cy), 16)
                pygame.draw.circle(pantalla, (80, 50, 20), (cx, cy), 16, 2)
                pygame.draw.circle(pantalla, (218, 165, 32), (cx, cy), 11)
                pygame.draw.circle(pantalla, (184, 134, 11), (cx, cy), 11, 2)
                pygame.draw.line(pantalla, (184, 134, 11), (cx, cy - 5), (cx, cy - 28), 4)
                pygame.draw.polygon(pantalla, (255, 215, 0), [
                    (cx, cy - 35),
                    (cx - 5, cy - 25),
                    (cx + 5, cy - 25)
                ])
                pygame.draw.arc(pantalla, (139, 90, 43), (cx - 12, cy - 20, 24, 14), 3.14, 6.28, 3)

            elif d.tipo == "muro":
                pygame.draw.rect(pantalla, d.color, (x + 2, y + 2, 36, 36), border_radius=4)
                pygame.draw.rect(pantalla, (100, 100, 100), (x + 2, y + 2, 36, 36), 3)

            bx = x + 2
            by = y - 8
            bw = 36
            bh = 5
            pygame.draw.rect(pantalla, ROJO, (bx, by, bw, bh))
            vida_w = int(bw * (d.vida / d.vida_max))
            pygame.draw.rect(pantalla, VERDE, (bx, by, vida_w, bh))

    def _proyectiles(self, pantalla, proyectiles):
        for p in proyectiles:
            px = int(p.x)
            py = int(p.y) + 70
            pygame.draw.circle(pantalla, (255, 255, 200), (px, py), 5)
            pygame.draw.circle(pantalla, (255, 255, 0), (px, py), 3)

    def _ui(self, pantalla, oleada, puntuacion, oro, tipo_defensa, jugador, fuente):
        panel = pygame.Rect(0, 0, 800, 70)
        pygame.draw.rect(pantalla, (15, 15, 25), panel)
        pygame.draw.line(pantalla, (60, 60, 80), (0, 70), (800, 70), 1)

        texto_oleada = fuente.render(f"Oleada: {oleada}", True, (255, 255, 255))
        texto_puntos = fuente.render(f"Pts: {puntuacion}", True, (255, 255, 255))
        texto_oro = fuente.render(f"Oro: {oro}", True, (255, 215, 0))
        ## FASE 12 - Nombre del jugador abajo a la izquierda
        texto_jugador = fuente.render(f"{jugador}", True, (200, 200, 255))
        ## FIN FASE 12
        pantalla.blit(texto_oleada, (10, 8))
        pantalla.blit(texto_puntos, (160, 8))
        pantalla.blit(texto_oro, (300, 8))
        pantalla.blit(texto_jugador, (10, 40))

        ## FASE 12 - Defensas movidas a la derecha
        opciones = [
            ("Valla", (139, 90, 43), 530, Defensa.COSTOS["valla"]),
            ("Torre", (100, 100, 150), 620, Defensa.COSTOS["torre"]),
            ("Muro", (80, 80, 80), 710, Defensa.COSTOS["muro"]),
        ]
        ## FIN FASE 12
        for nombre, color, x, costo in opciones:
            rect = pygame.Rect(x, 12, 36, 36)

            if nombre == "Valla":
                vx = x + 2
                vy = 12
                for i in range(4):
                    px = vx + 4 + i * 8
                    pygame.draw.line(pantalla, (139, 90, 43), (px, vy + 4), (px, vy + 32), 2)
                pygame.draw.line(pantalla, (139, 90, 43), (vx + 2, vy + 10), (vx + 34, vy + 10), 2)
                pygame.draw.line(pantalla, (139, 90, 43), (vx + 2, vy + 24), (vx + 34, vy + 24), 2)
                if nombre.lower() == tipo_defensa:
                    pygame.draw.rect(pantalla, (255, 255, 255), (x, 12, 36, 36), 2)

            elif nombre == "Torre":
                cx = x + 18
                cy = 30
                pygame.draw.circle(pantalla, (101, 67, 33), (cx, cy), 12)
                pygame.draw.circle(pantalla, (218, 165, 32), (cx, cy), 8)
                pygame.draw.line(pantalla, (184, 134, 11), (cx, cy - 4), (cx, cy - 18), 3)
                pygame.draw.polygon(pantalla, (255, 215, 0), [(cx, cy - 22), (cx - 4, cy - 15), (cx + 4, cy - 15)])
                if nombre.lower() == tipo_defensa:
                    pygame.draw.circle(pantalla, (255, 255, 255), (cx, cy), 13, 2)

            else:
                pygame.draw.rect(pantalla, color, rect)
                if nombre.lower() == tipo_defensa:
                    pygame.draw.rect(pantalla, (255, 255, 255), rect, 3)
                else:
                    pygame.draw.rect(pantalla, (100, 100, 100), rect, 1)

            texto_nombre = fuente.render(f"{nombre} ${costo}", True, (200, 200, 200))
            pantalla.blit(texto_nombre, (x, 50))

    def _pantalla_menu(self, pantalla, fuente_grande, fuente, tabla_hash = None):
        # Fondo con degradado
        for i in range(670):
            color = (15 + i // 10, 10 + i // 15, 25 + i // 8)
            pygame.draw.line(pantalla, color, (0, i), (800, i))

        # Título con sombra
        sombra = fuente_grande.render("DEFENSA DE LA FOGATA", True, (0, 0, 0))
        pantalla.blit(sombra, sombra.get_rect(center=(403, 153)))
        titulo = fuente_grande.render("DEFENSA DE LA FOGATA", True, (255, 200, 50))
        pantalla.blit(titulo, titulo.get_rect(center=(400, 150)))

        # Subtítulo
        subtitulo = fuente.render("Protege la fogata de las criaturas", True, (200, 200, 200))
        pantalla.blit(subtitulo, subtitulo.get_rect(center=(400, 220)))

        # Instrucciones
        instrucciones = [
            "1, 2, 3 = Seleccionar defensa",
            "Click = Colocar defensa",
            "R = Reiniciar al terminar",
        ]
        for i, texto in enumerate(instrucciones):
            surf = fuente.render(texto, True, (180, 180, 180))
            pantalla.blit(surf, surf.get_rect(center=(400, 270 + i * 30)))

        # Botón JUGAR con efecto hover
        mouse_x, mouse_y = pygame.mouse.get_pos()
        boton = pygame.Rect(300, 420, 200, 70)
        if boton.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(pantalla, (0, 200, 0), boton, border_radius=15)
        else:
            pygame.draw.rect(pantalla, (0, 150, 0), boton, border_radius=15)
        pygame.draw.rect(pantalla, (255, 255, 255), boton, 3, border_radius=15)
        texto_jugar = fuente_grande.render("JUGAR", True, (255, 255, 255))
        pantalla.blit(texto_jugar, texto_jugar.get_rect(center=boton.center))


    def _pantalla_final(self, pantalla, victoria, jugador, puntuacion, fuente_grande, fuente):
        overlay = pygame.Surface((800, 670))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))

        if victoria:
            texto = fuente_grande.render("¡VICTORIA!", True, (0, 255, 0))
            detalle = fuente.render(f"{jugador}, salvaste la fogata", True, (200, 255, 200))
        else:
            texto = fuente_grande.render("GAME OVER", True, (255, 0, 0))
            detalle = fuente.render(f"{jugador}, la fogata fue destruida", True, (255, 200, 200))

        pantalla.blit(texto, texto.get_rect(center=(400, 250)))
        pantalla.blit(detalle, detalle.get_rect(center=(400, 310)))

        puntos_texto = fuente.render(f"Puntuacion final: {puntuacion}", True, (255, 255, 0))
        pantalla.blit(puntos_texto, puntos_texto.get_rect(center=(400, 360)))

        texto_r = fuente.render("Presiona R para reiniciar", True, (255, 255, 255))
        pantalla.blit(texto_r, texto_r.get_rect(center=(400, 420)))

        ## FASE 12 - Pantalla de pausa
    def _pantalla_pausa(self, pantalla, fuente_grande):
        overlay = pygame.Surface((800, 670))
        overlay.set_alpha(160)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))

        texto = fuente_grande.render("PAUSA", True, (255, 255, 255))
        pantalla.blit(texto, texto.get_rect(center=(400, 300)))

        texto_p = fuente_grande.render("Presiona P para continuar", True, (200, 200, 200))
        pantalla.blit(texto_p, texto_p.get_rect(center=(400, 370)))
    ## FIN FASE 12