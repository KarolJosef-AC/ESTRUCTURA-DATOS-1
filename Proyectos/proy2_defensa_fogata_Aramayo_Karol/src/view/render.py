"""
Vista del juego. Solo dibuja, no piensa.
Fase: 12 - Panel del planificador visible en juego.

Ventana: 1000x670
    - Mapa: 0..799 (800px, 20 celdas x 40px)
    - Panel planificador: 800..999 (200px)
    - HUD superior: 70px de alto
"""

import pygame
from model.mapa import Mapa, TAM_CELDA, CELDA_LIBRE
from model.entidades.fogata import Fogata
from model.entidades.defensa import Defensa

# ── Paleta ───────────────────────────────────────────────────────────────────
FONDO_OSCURO  = (18,  14,  10)
CARBON        = (32,  26,  20)
CARBON_MED    = (44,  36,  26)
BRASA         = (180, 70,  10)
BRASA_CLARO   = (220, 100, 20)
LLAMA         = (255, 160, 30)
LLAMA_VIVA    = (255, 210, 80)
CENIZA        = (110, 100, 90)
CENIZA_CLARA  = (150, 140, 125)
MARFIL        = (230, 220, 200)
MARFIL_TENUE  = (160, 150, 135)
VERDE_VIDA    = (80,  200, 80)
ROJO_DANO     = (200, 40,  40)
DORADO        = (218, 165, 32)

ALTO_HUD    = 70
ANCHO_MAPA  = 800   # 20 celdas * 40px
ANCHO_PANEL = 200   # panel del planificador
ANCHO_TOTAL = ANCHO_MAPA + ANCHO_PANEL  # 1000px

# Colores por prioridad en el panel
COLOR_P = {
    0: (255, 90,  90),   # CRITICO - rojo
    1: (255, 180, 60),   # ALTO    - naranja
    2: (160, 160, 220),  # NORMAL  - azul claro
    3: (130, 130, 130),  # BAJO    - gris
}


class Render:
    """
    Renderizador principal del juego.
    Ventana 1000x670: mapa (800px) + panel planificador (200px).
    """

    def __init__(self):
        """Inicializa el render con historial acumulado del planificador."""
        # Cada entrada es (prioridad, descripcion) o None = separador de frame
        self._historial_log = []
        self._frame_panel   = 0

    # ── Actualizar historial desde el planificador ────────────────────────────

    def actualizar_historial(self, acciones: list) -> None:
        """
        Acumula las acciones del frame en el log del panel.
        Agrega un separador entre frames para imitar la terminal.
        Mantiene un máximo de 200 entradas para no crecer infinito.

        Args:
            acciones: Lista de AccionJuego del frame actual.
        """
        if not acciones:
            return

        self._frame_panel += 1

        # Separador de frame con número
        self._historial_log.append(
            ("sep", f"Frame {self._frame_panel} ({len(acciones)} acc)"))

        for a in acciones:
            self._historial_log.append((a.prioridad, a.descripcion))

        # Limitar tamaño del log
        if len(self._historial_log) > 220:
            self._historial_log = self._historial_log[-200:]

    # ── Método principal ──────────────────────────────────────────────────────

    def dibujar(self, pantalla, mapa, fogata, enemigos, defensas, proyectiles,
                oleada, puntuacion, oro, tipo_defensa, jugador, estado, fuente,
                fuente_grande, tabla_hash=None, pausa=False):
        """Punto de entrada del renderizado."""
        pantalla.fill(FONDO_OSCURO)

        if estado == "menu":
            self._pantalla_menu(pantalla, fuente_grande, fuente, tabla_hash)
            return

        # Zona del mapa (0..799)
        self._grilla(pantalla, mapa)
        self._fogata(pantalla, fogata)
        self._enemigos(pantalla, enemigos)
        self._defensas(pantalla, defensas)
        self._proyectiles(pantalla, proyectiles)
        self._ui(pantalla, oleada, puntuacion, oro, tipo_defensa,
                 jugador, fuente, fogata)

        # Panel del planificador (800..999)
        self._panel_planificador(pantalla, fuente)

        if estado == "jugando" and pausa:
            self._pantalla_pausa(pantalla, fuente_grande, fuente)

        if estado == "fin_derrota":
            self._pantalla_final(pantalla, jugador, puntuacion,
                                 fuente_grande, fuente, oleada, tabla_hash)

    # ── Grid ─────────────────────────────────────────────────────────────────

    def _grilla(self, pantalla, mapa):
        """Dibuja la cuadrícula 20x15 con tablero ajedrezado."""
        for fila in range(mapa.filas):
            for col in range(mapa.columnas):
                tipo = mapa.obtener(col, fila)
                x = col * TAM_CELDA
                y = fila * TAM_CELDA + ALTO_HUD
                rect = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)
                if tipo == CELDA_LIBRE:
                    color = CARBON if (col + fila) % 2 == 0 else CARBON_MED
                    pygame.draw.rect(pantalla, color, rect)
                pygame.draw.rect(pantalla, (50, 42, 32), rect, width=1)

    # ── Fogata ────────────────────────────────────────────────────────────────

    def _fogata(self, pantalla, fogata):
        """Dibuja la fogata con fuego multicapa y barra de vida."""
        x  = fogata.col * TAM_CELDA
        y  = fogata.fila * TAM_CELDA + ALTO_HUD
        w  = fogata.ancho * TAM_CELDA
        h  = fogata.alto * TAM_CELDA
        cx = x + w // 2
        cy = y + h // 2

        glow = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.circle(glow, (255, 100, 0, 30), (50, 50), 48)
        pygame.draw.circle(glow, (255, 140, 0, 20), (50, 50), 38)
        pantalla.blit(glow, (cx - 50, cy - 50))

        pygame.draw.rect(pantalla, (90, 55, 25),
                         pygame.Rect(x + 6, y + h - 14, w - 12, 12),
                         border_radius=3)
        pygame.draw.circle(pantalla, (200, 50,  0),  (cx, cy + 2),  20)
        pygame.draw.circle(pantalla, (255, 100, 0),  (cx, cy - 2),  16)
        pygame.draw.circle(pantalla, (255, 160, 0),  (cx - 2, cy - 7),  11)
        pygame.draw.circle(pantalla, (255, 220, 80), (cx + 2, cy - 12),  6)
        pygame.draw.circle(pantalla, (255, 255, 200),(cx, cy - 16),  3)

        vida_pct = fogata.porcentaje_vida()
        bx, by = x - 4, y - 16
        bw, bh = w + 8, 8
        pygame.draw.rect(pantalla, (40, 20, 20),
                         pygame.Rect(bx, by, bw, bh), border_radius=4)
        if vida_pct > 0:
            pygame.draw.rect(pantalla, self._color_vida(vida_pct),
                             pygame.Rect(bx, by, int(bw * vida_pct), bh),
                             border_radius=4)
        pygame.draw.rect(pantalla, CENIZA,
                         pygame.Rect(bx, by, bw, bh), 1, border_radius=4)

    # ── Enemigos ──────────────────────────────────────────────────────────────

    def _enemigos(self, pantalla, enemigos):
        """Dibuja cada enemigo diferenciado por tipo."""
        for enemigo in enemigos:
            x = enemigo.col * TAM_CELDA + TAM_CELDA // 2
            y = int(enemigo.y) + ALTO_HUD + TAM_CELDA // 2

            if enemigo.tipo == "normal":
                pygame.draw.circle(pantalla, (140, 30, 30), (x, y), 17)
                pygame.draw.circle(pantalla, enemigo.color, (x, y), 15)
                pygame.draw.circle(pantalla, (255, 240, 220), (x - 5, y - 4), 5)
                pygame.draw.circle(pantalla, (255, 240, 220), (x + 5, y - 4), 5)
                pygame.draw.circle(pantalla, (20, 0, 0),  (x - 5, y - 4), 2)
                pygame.draw.circle(pantalla, (20, 0, 0),  (x + 5, y - 4), 2)
                pygame.draw.arc(pantalla, (200, 20, 20),
                                (x - 5, y + 2, 10, 6), 3.14, 6.28, 2)
            elif enemigo.tipo == "tanque":
                pygame.draw.rect(pantalla, (50, 20, 60),
                                 pygame.Rect(x - 15, y - 13, 32, 30),
                                 border_radius=5)
                pygame.draw.rect(pantalla, enemigo.color,
                                 pygame.Rect(x - 16, y - 15, 32, 30),
                                 border_radius=6)
                pygame.draw.rect(pantalla, (130, 60, 130),
                                 pygame.Rect(x - 10, y - 9, 20, 14),
                                 border_radius=3)
                pygame.draw.circle(pantalla, (255, 200, 0), (x - 6, y - 5), 4)
                pygame.draw.circle(pantalla, (255, 200, 0), (x + 6, y - 5), 4)
                pygame.draw.circle(pantalla, (80, 0, 80),  (x - 6, y - 5), 2)
                pygame.draw.circle(pantalla, (80, 0, 80),  (x + 6, y - 5), 2)
            elif enemigo.tipo == "rapido":
                pts  = [(x, y-16),(x+12, y),(x, y+12),(x-12, y)]
                pts2 = [(x, y-13),(x+10, y),(x, y+10),(x-10, y)]
                pygame.draw.polygon(pantalla, (90, 0, 110), pts)
                pygame.draw.polygon(pantalla, enemigo.color, pts2)
                pygame.draw.circle(pantalla, (255, 255, 255), (x, y - 2), 4)
                pygame.draw.circle(pantalla, (0, 0, 0),       (x, y - 2), 2)

            # Barra de vida
            bx2, by2 = x - 16, y - 26
            bw, bh = 32, 4
            pygame.draw.rect(pantalla, (50, 20, 20),
                             pygame.Rect(bx2, by2, bw, bh), border_radius=2)
            vida_w = int(bw * enemigo.porcentaje_vida())
            if vida_w > 0:
                pygame.draw.rect(pantalla,
                                 self._color_vida(enemigo.porcentaje_vida()),
                                 pygame.Rect(bx2, by2, vida_w, bh),
                                 border_radius=2)

    # ── Defensas ──────────────────────────────────────────────────────────────

    def _defensas(self, pantalla, defensas):
        """Dibuja cada defensa."""
        for d in defensas:
            x = d.col * TAM_CELDA
            y = d.fila * TAM_CELDA + ALTO_HUD

            if d.tipo == "valla":
                for i in range(4):
                    px = x + 5 + i * 10
                    pygame.draw.line(pantalla, (110, 68, 28),
                                     (px, y + 4), (px, y + 36), 4)
                    pygame.draw.line(pantalla, (160, 100, 50),
                                     (px, y + 4), (px, y + 36), 2)
                pygame.draw.line(pantalla, (130, 82, 35),
                                 (x + 3, y + 13), (x + 37, y + 13), 3)
                pygame.draw.line(pantalla, (130, 82, 35),
                                 (x + 3, y + 27), (x + 37, y + 27), 3)
            elif d.tipo == "torre":
                cx2, cy2 = x + 20, y + 20
                pygame.draw.circle(pantalla, (80, 50, 20),  (cx2, cy2), 17)
                pygame.draw.circle(pantalla, (101, 67, 33), (cx2, cy2), 15)
                pygame.draw.circle(pantalla, (184, 134, 11),(cx2, cy2), 10)
                pygame.draw.circle(pantalla, DORADO,        (cx2, cy2),  8)
                pygame.draw.line(pantalla, (140, 100, 30),
                                 (cx2, cy2 - 4), (cx2, cy2 - 26), 5)
                pygame.draw.line(pantalla, (200, 160, 50),
                                 (cx2, cy2 - 4), (cx2, cy2 - 26), 3)
                pygame.draw.polygon(pantalla, LLAMA_VIVA, [
                    (cx2, cy2-32),(cx2-5, cy2-22),(cx2+5, cy2-22)])
            elif d.tipo == "muro":
                pygame.draw.rect(pantalla, (55, 55, 58),
                                 pygame.Rect(x+1, y+1, 38, 38), border_radius=5)
                pygame.draw.rect(pantalla, (75, 75, 80),
                                 pygame.Rect(x+3, y+3, 34, 34), border_radius=4)
                pygame.draw.line(pantalla, (55,55,58),(x+3,y+20),(x+37,y+20),2)
                pygame.draw.line(pantalla, (55,55,58),(x+20,y+3),(x+20,y+19),2)
                pygame.draw.line(pantalla, (55,55,58),(x+10,y+21),(x+10,y+37),2)
                pygame.draw.line(pantalla, (55,55,58),(x+30,y+21),(x+30,y+37),2)
                pygame.draw.rect(pantalla, (95, 95, 100),
                                 pygame.Rect(x+1, y+1, 38, 38), 2,
                                 border_radius=5)

            bx2, by2 = x + 2, y - 9
            bw, bh = 36, 5
            pygame.draw.rect(pantalla, (40, 20, 20),
                             pygame.Rect(bx2, by2, bw, bh), border_radius=2)
            vida_w = int(bw * (d.vida / d.vida_max))
            if vida_w > 0:
                pygame.draw.rect(pantalla,
                                 self._color_vida(d.vida / d.vida_max),
                                 pygame.Rect(bx2, by2, vida_w, bh),
                                 border_radius=2)

    # ── Proyectiles ───────────────────────────────────────────────────────────

    def _proyectiles(self, pantalla, proyectiles):
        """Dibuja proyectiles como brasas con halo."""
        for p in proyectiles:
            px, py = int(p.x), int(p.y) + ALTO_HUD
            pygame.draw.circle(pantalla, (200, 100, 0), (px, py), 6)
            pygame.draw.circle(pantalla, (255, 230, 100), (px, py), 4)
            pygame.draw.circle(pantalla, (255, 255, 240), (px, py), 2)

    # ── HUD ───────────────────────────────────────────────────────────────────

    def _ui(self, pantalla, oleada, puntuacion, oro, tipo_defensa,
            jugador, fuente, fogata):
        """Panel HUD superior (solo sobre el mapa, 800px de ancho)."""
        pygame.draw.rect(pantalla, (22, 18, 12),
                         pygame.Rect(0, 0, ANCHO_MAPA, ALTO_HUD))
        pygame.draw.rect(pantalla, (30, 24, 16),
                         pygame.Rect(0, 0, ANCHO_MAPA, 36))
        pygame.draw.line(pantalla, BRASA,
                         (0, ALTO_HUD - 2), (ANCHO_MAPA, ALTO_HUD - 2), 2)

        self._etiqueta_valor(pantalla, fuente, "OLEADA", str(oleada),
                             10, 6, CENIZA_CLARA, MARFIL)
        self._etiqueta_valor(pantalla, fuente, "PTS", str(puntuacion),
                             110, 6, CENIZA_CLARA, LLAMA_VIVA)
        self._etiqueta_valor(pantalla, fuente, "ORO", str(oro),
                             220, 6, CENIZA_CLARA, DORADO)
        self._barra_fogata_hud(pantalla, fuente, fogata, 330, 8)

        if jugador:
            surf = fuente.render(f"  {jugador}", True, MARFIL_TENUE)
            pantalla.blit(surf, (10, 44))

        opciones = [
            ("1", "Valla", "valla", 530, Defensa.COSTOS["valla"]),
            ("2", "Torre", "torre", 625, Defensa.COSTOS["torre"]),
            ("3", "Muro",  "muro",  720, Defensa.COSTOS["muro"]),
        ]
        for tecla, nombre, clave, ox, costo in opciones:
            self._selector_defensa(pantalla, fuente, tecla, nombre,
                                   clave, ox, costo, clave == tipo_defensa)

    def _etiqueta_valor(self, pantalla, fuente, etiqueta, valor,
                         x, y, color_et, color_val):
        """Etiqueta pequeña encima de valor grande."""
        f18 = pygame.font.Font(None, 18)
        pantalla.blit(f18.render(etiqueta, True, color_et), (x, y))
        pantalla.blit(fuente.render(valor, True, color_val),  (x, y + 14))

    def _barra_fogata_hud(self, pantalla, fuente, fogata, x, y):
        """Barra de vida de la fogata en el HUD."""
        f18 = pygame.font.Font(None, 18)
        pantalla.blit(f18.render("FOGATA", True, CENIZA_CLARA), (x, y))
        bx, by2 = x, y + 14
        bw, bh  = 160, 12
        pct = fogata.porcentaje_vida()
        pygame.draw.rect(pantalla, (40, 20, 10),
                         pygame.Rect(bx, by2, bw, bh), border_radius=6)
        if pct > 0:
            pygame.draw.rect(pantalla, self._color_vida(pct),
                             pygame.Rect(bx, by2, int(bw * pct), bh),
                             border_radius=6)
        pygame.draw.rect(pantalla, BRASA,
                         pygame.Rect(bx, by2, bw, bh), 1, border_radius=6)
        pantalla.blit(f18.render(f"{int(pct*100)}%", True, MARFIL_TENUE),
                      (bx + bw + 6, by2))

    def _selector_defensa(self, pantalla, fuente, tecla, nombre,
                           clave, x, costo, seleccionado):
        """Selector de defensa con ícono, tecla y costo."""
        f18 = pygame.font.Font(None, 18)
        color_fondo = (50, 38, 22) if seleccionado else (26, 20, 14)
        color_borde = BRASA       if seleccionado else (55, 45, 32)
        pygame.draw.rect(pantalla, color_fondo,
                         pygame.Rect(x - 4, 2, 80, 58), border_radius=6)
        pygame.draw.rect(pantalla, color_borde,
                         pygame.Rect(x - 4, 2, 80, 58), 2, border_radius=6)
        self._icono_defensa(pantalla, clave, x + 20, 22)
        pantalla.blit(f18.render(f"[{tecla}]", True,
                      LLAMA if seleccionado else CENIZA), (x - 2, 4))
        pantalla.blit(f18.render(f"${costo}", True,
                      DORADO if seleccionado else MARFIL_TENUE), (x + 38, 4))
        pantalla.blit(f18.render(nombre, True,
                      MARFIL if seleccionado else MARFIL_TENUE), (x + 2, 46))

    def _icono_defensa(self, pantalla, tipo, cx, cy):
        """Ícono mini de defensa para el selector."""
        if tipo == "valla":
            for i in range(3):
                px = cx - 10 + i * 10
                pygame.draw.line(pantalla,(160,100,50),(px,cy-10),(px,cy+10),3)
            pygame.draw.line(pantalla,(130,82,35),(cx-12,cy-3),(cx+12,cy-3),2)
            pygame.draw.line(pantalla,(130,82,35),(cx-12,cy+5),(cx+12,cy+5),2)
        elif tipo == "torre":
            pygame.draw.circle(pantalla,(101,67,33),(cx,cy+4),10)
            pygame.draw.circle(pantalla,DORADO,(cx,cy+4),7)
            pygame.draw.line(pantalla,(200,160,50),(cx,cy-4),(cx,cy-14),3)
            pygame.draw.polygon(pantalla,LLAMA_VIVA,
                                [(cx,cy-18),(cx-4,cy-11),(cx+4,cy-11)])
        elif tipo == "muro":
            pygame.draw.rect(pantalla,(75,75,80),
                             pygame.Rect(cx-12,cy-12,24,24),border_radius=3)
            pygame.draw.rect(pantalla,(95,95,100),
                             pygame.Rect(cx-12,cy-12,24,24),2,border_radius=3)

    # ── Panel Planificador ────────────────────────────────────────────────────

    def _panel_planificador(self, pantalla, fuente):
        """
        Panel lateral derecho (x=800..999).
        Log acumulado de frames con separador --- entre cada uno.
        Auto-scroll: siempre muestra las líneas más recientes.
        Colores claros para proyección.
        """
        px = ANCHO_MAPA
        pw = ANCHO_PANEL
        ph = 670

        # Fondo gris oscuro (no negro: más legible en proyector)
        pygame.draw.rect(pantalla, (28, 28, 32),
                         pygame.Rect(px, 0, pw, ph))
        pygame.draw.line(pantalla, (100, 80, 50),
                         (px, 0), (px, ph), 2)

        f13 = pygame.font.Font(None, 13)
        f18 = pygame.font.Font(None, 18)

        # Título
        titulo = f18.render("PLANIFICADOR", True, (255, 255, 255))
        pantalla.blit(titulo, (px + 6, 6))
        pygame.draw.line(pantalla, (90, 80, 60),
                         (px + 4, 26), (px + pw - 4, 26), 1)

        # Leyenda compacta con colores claros
        leyenda = [
            (0, "[0] CRITICO", (255, 120, 120)),
            (1, "[1] ALTO",    (255, 210,  80)),
            (2, "[2] NORMAL",  (130, 200, 255)),
            (3, "[3] BAJO",    (190, 190, 190)),
        ]
        for i, (_, texto, color) in enumerate(leyenda):
            y_ley = 30 + i * 13
            pygame.draw.circle(pantalla, color, (px + 8, y_ley + 5), 3)
            pantalla.blit(f13.render(texto, True, color), (px + 14, y_ley))

        pygame.draw.line(pantalla, (90, 80, 60),
                         (px + 4, 84), (px + pw - 4, 84), 1)

        # Zona del log — auto-scroll a las líneas más recientes
        y_start = 88
        line_h  = 13
        max_vis = (ph - y_start - 4) // line_h
        log = self._historial_log[-max_vis:] if self._historial_log else []

        if not log:
            pantalla.blit(f13.render("(esperando acciones...)",
                                     True, (160, 160, 160)),
                          (px + 6, y_start))
        else:
            for i, entrada in enumerate(log):
                y_lin = y_start + i * line_h
                tipo, texto = entrada

                if tipo == "sep":
                    # Separador de frame: línea + "--- Frame N (X acc)"
                    pygame.draw.line(pantalla, (70, 65, 55),
                                     (px + 4, y_lin + 6),
                                     (px + pw - 4, y_lin + 6), 1)
                    pantalla.blit(f13.render(texto, True, (200, 160, 80)),
                                  (px + 6, y_lin))
                else:
                    prioridad = tipo
                    color_p = {
                        0: (255, 120, 120),
                        1: (255, 210,  80),
                        2: (130, 200, 255),
                        3: (190, 190, 190),
                    }.get(prioridad, (200, 200, 200))

                    pantalla.blit(
                        f13.render(f"[{prioridad}]", True, color_p),
                        (px + 6, y_lin))
                    desc = (texto if len(texto) <= 15
                            else texto[:14] + ".")
                    pantalla.blit(
                        f13.render(desc, True, (220, 220, 220)),
                        (px + 26, y_lin))

    # ── Pantallas ─────────────────────────────────────────────────────────────

    def _pantalla_menu(self, pantalla, fuente_grande, fuente, tabla_hash=None):
        """Pantalla de menú principal (ocupa toda la ventana 1000px)."""
        pantalla.fill(FONDO_OSCURO)
        pygame.draw.line(pantalla, BRASA,      (120, 200), (880, 200), 1)
        pygame.draw.line(pantalla, BRASA_CLARO,(220, 202), (780, 202), 1)

        sombra = fuente_grande.render("DEFENSA DE LA FOGATA", True, (80, 30, 0))
        titulo  = fuente_grande.render("DEFENSA DE LA FOGATA", True, LLAMA)
        pantalla.blit(sombra, sombra.get_rect(center=(502, 152)))
        pantalla.blit(titulo,  titulo.get_rect(center=(500, 150)))

        sub = fuente.render("Protege la fogata de las hordas enemigas",
                            True, CENIZA_CLARA)
        pantalla.blit(sub, sub.get_rect(center=(500, 215)))

        pygame.draw.line(pantalla, (50, 38, 22), (300, 240), (700, 240), 1)

        instrucciones = [
            "1 / 2 / 3  →  Seleccionar defensa",
            "Click      →  Colocar defensa",
            "P          →  Pausar",
            "R          →  Reiniciar al perder",
        ]
        f24 = pygame.font.Font(None, 24)
        for i, texto in enumerate(instrucciones):
            surf = f24.render(texto, True, MARFIL_TENUE)
            pantalla.blit(surf, surf.get_rect(center=(500, 268 + i * 28)))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        boton = pygame.Rect(400, 420, 200, 58)
        hover = boton.collidepoint(mouse_x, mouse_y)
        pygame.draw.rect(pantalla, BRASA_CLARO if hover else BRASA,
                         boton, border_radius=12)
        pygame.draw.rect(pantalla, LLAMA, boton, 2, border_radius=12)
        surf_jugar = fuente_grande.render("JUGAR", True,
                                          LLAMA_VIVA if hover else MARFIL)
        pantalla.blit(surf_jugar, surf_jugar.get_rect(center=boton.center))

        if tabla_hash:
            ranking = tabla_hash.obtener_todas()
            if ranking:
                f22 = pygame.font.Font(None, 22)
                surf_t = f22.render("— Mejores jugadores —", True, CENIZA)
                pantalla.blit(surf_t, surf_t.get_rect(center=(500, 500)))
                for i, (nombre, pts) in enumerate(ranking[:3]):
                    surf_r = f22.render(f"{i+1}. {nombre}  {pts} pts",
                                        True, MARFIL_TENUE)
                    pantalla.blit(surf_r,
                                  surf_r.get_rect(center=(500, 522 + i * 22)))

    def dibujar_login(self, pantalla, nombre_input, fuente, fuente_grande,
                       tabla_hash):
        """Pantalla de ingreso de nombre (ventana 1000px)."""
        pantalla.fill(FONDO_OSCURO)
        pygame.draw.line(pantalla, BRASA, (200, 185), (800, 185), 1)

        sombra = fuente_grande.render("DEFENSA DE LA FOGATA", True, (80,30,0))
        titulo  = fuente_grande.render("DEFENSA DE LA FOGATA", True, LLAMA)
        pantalla.blit(sombra, sombra.get_rect(center=(502, 142)))
        pantalla.blit(titulo,  titulo.get_rect(center=(500, 140)))

        f26 = pygame.font.Font(None, 26)
        pantalla.blit(
            f26.render("Ingresa tu nombre para comenzar", True, CENIZA_CLARA),
            f26.render("Ingresa tu nombre para comenzar",
                       True, CENIZA_CLARA).get_rect(center=(500, 210)))

        campo = pygame.Rect(250, 250, 500, 52)
        pygame.draw.rect(pantalla, (30, 22, 14), campo, border_radius=8)
        pygame.draw.rect(pantalla, BRASA, campo, 2, border_radius=8)
        surf_nom = fuente_grande.render(nombre_input + "_", True, LLAMA_VIVA)
        pantalla.blit(surf_nom, surf_nom.get_rect(center=campo.center))

        f22 = pygame.font.Font(None, 22)
        surf_inst = f22.render("ENTER = Jugar   |   ESC = Volver",
                               True, CENIZA)
        pantalla.blit(surf_inst, surf_inst.get_rect(center=(500, 322)))

        if nombre_input and tabla_hash.existe(nombre_input):
            pts = tabla_hash.obtener(nombre_input)
            surf_ex = f26.render(
                f"¡Bienvenido de vuelta! Mejor marca: {pts} pts",
                True, VERDE_VIDA)
            pantalla.blit(surf_ex, surf_ex.get_rect(center=(500, 360)))

        ranking = tabla_hash.obtener_todas()
        if ranking:
            pygame.draw.line(pantalla,(50,38,22),(250,390),(750,390),1)
            pantalla.blit(
                f26.render("Top 5 — Mejores puntajes", True, DORADO),
                f26.render("Top 5 — Mejores puntajes",
                           True, DORADO).get_rect(center=(500, 408)))
            for i, (nombre, pts) in enumerate(ranking[:5]):
                color = LLAMA if nombre == nombre_input else MARFIL_TENUE
                surf_r = f22.render(f"{i+1}.  {nombre}  —  {pts} pts",
                                    True, color)
                pantalla.blit(surf_r,
                              surf_r.get_rect(center=(500, 432 + i * 24)))

    def _pantalla_pausa(self, pantalla, fuente_grande, fuente):
        """Overlay de pausa."""
        overlay = pygame.Surface((ANCHO_TOTAL, 670), pygame.SRCALPHA)
        overlay.fill((10, 8, 5, 180))
        pantalla.blit(overlay, (0, 0))
        marco = pygame.Rect(300, 270, 400, 130)
        pygame.draw.rect(pantalla, (30, 22, 14), marco, border_radius=12)
        pygame.draw.rect(pantalla, BRASA, marco, 2, border_radius=12)
        surf_p = fuente_grande.render("PAUSA", True, LLAMA)
        pantalla.blit(surf_p, surf_p.get_rect(center=(500, 305)))
        f26 = pygame.font.Font(None, 26)
        surf_c = f26.render("Presiona P para continuar", True, CENIZA_CLARA)
        pantalla.blit(surf_c, surf_c.get_rect(center=(500, 360)))

    def _pantalla_final(self, pantalla, jugador, puntuacion,
                         fuente_grande, fuente, oleada, tabla_hash=None):
        """Pantalla de Game Over."""
        overlay = pygame.Surface((ANCHO_TOTAL, 670), pygame.SRCALPHA)
        overlay.fill((5, 2, 2, 210))
        pantalla.blit(overlay, (0, 0))

        marco = pygame.Rect(230, 180, 540, 310)
        pygame.draw.rect(pantalla, (28, 14, 14), marco, border_radius=14)
        pygame.draw.rect(pantalla, ROJO_DANO, marco, 2, border_radius=14)

        surf_go = fuente_grande.render("FOGATA APAGADA", True, ROJO_DANO)
        pantalla.blit(surf_go, surf_go.get_rect(center=(500, 218)))
        pygame.draw.line(pantalla, (80, 30, 30), (250, 248), (740, 248), 1)

        f28 = pygame.font.Font(None, 28)
        f22 = pygame.font.Font(None, 22)
        datos = [
            (f"Jugador:  {jugador}", MARFIL),
            (f"Puntuacion:  {puntuacion} pts", LLAMA_VIVA),
            (f"Oleada alcanzada:  {oleada}", CENIZA_CLARA),
        ]
        for i, (texto, color) in enumerate(datos):
            surf = f28.render(texto, True, color)
            pantalla.blit(surf, surf.get_rect(center=(500, 272 + i * 34)))

        if tabla_hash:
            ranking = tabla_hash.obtener_todas()
            if ranking:
                pygame.draw.line(pantalla,(80,30,30),(250,380),(740,380),1)
                pantalla.blit(
                    f22.render("— Mejores puntajes —", True, CENIZA),
                    f22.render("— Mejores puntajes —",
                               True, CENIZA).get_rect(center=(500, 396)))
                for i, (nombre, pts) in enumerate(ranking[:3]):
                    color = LLAMA if nombre == jugador else MARFIL_TENUE
                    surf_r = f22.render(f"{i+1}. {nombre}  {pts} pts",
                                        True, color)
                    pantalla.blit(surf_r,
                                  surf_r.get_rect(center=(500, 416 + i * 20)))

        surf_r = fuente.render("[ R ]  Reiniciar", True, CENIZA_CLARA)
        pantalla.blit(surf_r, surf_r.get_rect(center=(500, 468)))

    # ── Utilidad ──────────────────────────────────────────────────────────────

    def _color_vida(self, porcentaje: float) -> tuple:
        """Verde → amarillo → rojo según porcentaje de vida."""
        if porcentaje > 0.6:
            return VERDE_VIDA
        elif porcentaje > 0.3:
            return (220, 180, 0)
        return ROJO_DANO