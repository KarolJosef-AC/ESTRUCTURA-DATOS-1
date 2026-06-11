"""
Enemigo. Criatura que avanza hacia la fogata.

Fase: 3 - Movimiento de enemigos.
"""

from model.mapa import TAM_CELDA

class Enemigo:
    """Un enemigo que baja desde arriba hacia la fogata."""
    def __init__(self, col: int, fila:int , vida : int = 30, velocidad : float = 0.5):
        self.col = col
        self.fila = fila
        self.vida = vida
        self.vida_max = vida
        self.velocidad = velocidad

        self.x = col * TAM_CELDA
        self.y = fila * TAM_CELDA
        self._acumulado = 0.0

    def mover(self, dt: float, mapa) -> bool:
        """Avanza hacia abajo. Retorna True si llego al final."""
        self._acumulado += self.velocidad * dt

        celdas_avanzadas = 0
        while self._acumulado >= 1.0:
            self._acumulado -= 1.0
            celdas_avanzadas += 1

        if celdas_avanzadas > 0:
            nueva_fila = self.fila + celdas_avanzadas

            if nueva_fila >= mapa.filas:
                self.fila = mapa.filas - 1
                self.y = self.fila * TAM_CELDA
                return True

            self.fila = nueva_fila
            self.y = self.fila * TAM_CELDA

        return False
    
    def recibir_dano(self, cantidad:int ) -> None:
        self.vida = max(0, self.vida - cantidad)

    def esta_vivo(self) -> bool:
        return self.vida > 0
    
    def porcentaje_vida(self) -> float:
        return self.vida / self.vida_max
    