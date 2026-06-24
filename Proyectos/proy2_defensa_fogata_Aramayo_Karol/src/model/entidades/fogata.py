"""
Fogata. El objetivo que el jugador debe proteger.

Fase: 2 - Grid y fogata.
"""

from model.mapa import Mapa, CELDA_FOGATA, FILAS

COL_FOGATA = 9
FILA_FOGATA = FILAS - 1
ANCHO_FOGATA = 2
ALTO_FOGATA = 1
VIDA_MAXIMA = 100


class Fogata:
    """La fogata central. Si la destruyen, pierdes."""

    def __init__(self, mapa: Mapa) -> None:
        self.col = COL_FOGATA
        self.fila = FILA_FOGATA
        self.ancho = ANCHO_FOGATA
        self.alto = ALTO_FOGATA
        self.vida_maxima = VIDA_MAXIMA
        self.vida = self.vida_maxima

        mapa.marcar_zona(self.col, self.fila, self.ancho, self.alto, CELDA_FOGATA)

    def esta_viva(self) -> bool:
        return self.vida > 0

    def porcentaje_vida(self) -> float:
        return self.vida / self.vida_maxima

    def recibir_dano(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError(f"Daño negativo: {cantidad}")
        
        self.vida = max(0, self.vida - cantidad)