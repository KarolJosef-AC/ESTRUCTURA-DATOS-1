"""
Mapa del juego. Una cuadricula de celdas.

Fase: 2 - Grid y fogata.
Guarda que hay en cada celda: libre, obstaculo o fogata.
"""

COLUMNAS = 20
FILAS = 15
TAM_CELDA = 40

CELDA_LIBRE = 0
CELDA_OBSTACULO = 1
CELDA_FOGATA = 2


class Mapa:
    """Cuadricula de 20x15 que representa el terreno de juego."""

    def __init__(self) -> None:
        self.columnas = COLUMNAS
        self.filas = FILAS
        self.grilla = [
            [CELDA_LIBRE for _ in range(COLUMNAS)]
            for _ in range(FILAS)
        ]

    def obtener(self, col: int, fila: int) -> int:
        """Devuelve que hay en la celda (col, fila)."""
        if not self.dentro(col, fila):
            raise IndexError(f"Fuera del mapa: ({col}, {fila})")
        
        return self.grilla[fila][col]

    def dentro(self, col: int, fila: int) -> bool:
        """True si (col, fila) esta dentro del mapa."""
        return 0 <= col < self.columnas and 0 <= fila < self.filas

    def libre(self, col: int, fila: int) -> bool:
        """True si la celda esta vacia y se puede pasar."""
        return self.obtener(col, fila) == CELDA_LIBRE

    def poner(self, col: int, fila: int, tipo: int) -> None:
        """Cambia el tipo de una celda."""
        if tipo not in {CELDA_LIBRE, CELDA_OBSTACULO, CELDA_FOGATA}:
            raise ValueError(f"Tipo invalido: {tipo}")
        
        if not self.dentro(col, fila):
            raise IndexError(f"Fuera del mapa: ({col}, {fila})")
        
        self.grilla[fila][col] = tipo

    def marcar_zona(self, col: int, fila: int, ancho: int, alto: int, tipo: int) -> None:
        """Marca un bloque de celdas con un tipo."""
        for f in range(fila, fila + alto):
            for c in range(col, col + ancho):
                self.poner(c, f, tipo)