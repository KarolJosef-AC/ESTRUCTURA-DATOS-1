"""
Proyectil. Bala que disparan las torres.

Fase: 6 - Combate.
"""

from model.mapa import TAM_CELDA

class Proyectil:
    """Un proyectil que viaja hacia un enemigo"""
    def __init__(self, col:int , fila:int, enemigo, dano:int = 15, velocidad: float = 8):
        self.col = col
        self.fila = fila
        self.x = col * TAM_CELDA + TAM_CELDA // 2
        self.y = fila * TAM_CELDA + TAM_CELDA // 2
        self.enemigo = enemigo
        self.dano = dano
        self.velocidad = velocidad
        self.activo = True

    def mover(self, dt: float) -> None:
        """ Avanza hacia el enemigo objetivo."""
        if not self.enemigo.esta_vivo():
            self.activo = False
            return
        # calcular direccion hacia el enemigo
        dx = self.enemigo.x + TAM_CELDA // 2 - self.x
        dy = self.enemigo.y + TAM_CELDA // 2 - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia < 5:
            self.enemigo.recibir_dano(self.dano)
            self.activo = False
            return
        
        # mover hacia el enemigo
        self.x += (dx / distancia) * self.velocidad * dt * 60
        self.y += (dy / distancia) * self.velocidad * dt * 60

    def fuera_de_pantalla(self) -> bool:
        """ True si salio de la pantalla"""
        return self.x < 0 or self.x > 800 or self.y < 0 or self.y > 670
    
        