"""
Mapa del juego. Una cuadricula de celdas.
==========================================
Fase: 2 - Grid y fogata.

Representa el terreno de juego como una matriz de 20x15.
Cada celda puede estar: libre, con obstáculo o con fogata.
"""

COLUMNAS = 20
FILAS = 15
TAM_CELDA = 40

# REPRESENTACION DE TERRENO
CELDA_LIBRE = 0
CELDA_OBSTACULO = 1
CELDA_FOGATA = 2


class Mapa:
    """
    Cuadricula de 20x15 que representa el terreno de juego.
    
    Atributos:
        columnas (int): Número de columnas (20).
        filas (int): Número de filas (15).
        grilla (list): Matriz de celdas con valores 0, 1 o 2.
    """

    def __init__(self) -> None:
        """Inicializa la grilla con todas las celdas libres."""
        self.columnas = COLUMNAS
        self.filas = FILAS
        self.grilla = [
            [CELDA_LIBRE for _ in range(COLUMNAS)]
            for _ in range(FILAS)
        ]

    def obtener(self, col: int, fila: int) -> int:
        """
        Devuelve el valor de la celda en (col, fila).
        
        Args:
            col: Columna (0-19).
            fila: Fila (0-14).
            
        Returns:
            int: CELDA_LIBRE (0), CELDA_OBSTACULO (1) o CELDA_FOGATA (2).
            
        Raises:
            IndexError: Si la posición está fuera del mapa.
        """
        if not self.dentro(col, fila):
            raise IndexError(f"Fuera del mapa: ({col}, {fila})")
        return self.grilla[fila][col]

    def dentro(self, col: int, fila: int) -> bool:
        """
        Verifica si (col, fila) está dentro de los límites del mapa.
        
        Args:
            col: Columna a verificar.
            fila: Fila a verificar.
            
        Returns:
            bool: True si está dentro del mapa.
        """
        return 0 <= col < self.columnas and 0 <= fila < self.filas

    def libre(self, col: int, fila: int) -> bool:
        """
        Verifica si la celda está vacía y se puede ocupar.
        
        Args:
            col: Columna a verificar.
            fila: Fila a verificar.
            
        Returns:
            bool: True si la celda está libre.
        """
        return self.obtener(col, fila) == CELDA_LIBRE

    def poner(self, col: int, fila: int, tipo: int) -> None:
        """
        Cambia el tipo de una celda específica.
        
        Args:
            col: Columna de la celda.
            fila: Fila de la celda.
            tipo: Nuevo tipo (CELDA_LIBRE, CELDA_OBSTACULO, CELDA_FOGATA).
            
        Raises:
            ValueError: Si el tipo no es válido.
            IndexError: Si la posición está fuera del mapa.
        """
        if tipo not in {CELDA_LIBRE, CELDA_OBSTACULO, CELDA_FOGATA}:
            raise ValueError(f"Tipo invalido: {tipo}")
        if not self.dentro(col, fila):
            raise IndexError(f"Fuera del mapa: ({col}, {fila})")
        self.grilla[fila][col] = tipo

    def marcar_zona(self, col: int, fila: int, ancho: int, alto: int, tipo: int) -> None:
        """
        Marca un bloque rectangular de celdas con un tipo.
        Usado para colocar la fogata (2 celdas de ancho x 1 de alto).
        
        Args:
            col: Columna inicial.
            fila: Fila inicial.
            ancho: Número de columnas a marcar.
            alto: Número de filas a marcar.
            tipo: Tipo de celda a asignar.
        """
        for f in range(fila, fila + alto):
            for c in range(col, col + ancho):
                self.poner(c, f, tipo)
