"""
Fogata. El objetivo que el jugador debe proteger.
===================================================
Fase: 2 - Grid y fogata.

La fogata es el núcleo del juego. Si los enemigos la destruyen,
el jugador pierde la partida.
"""

from model.mapa import Mapa, CELDA_FOGATA, FILAS

COL_FOGATA = 9
FILA_FOGATA = FILAS - 1
ANCHO_FOGATA = 2
ALTO_FOGATA = 1
VIDA_MAXIMA = 100


class Fogata:
    """
    La fogata central que el jugador debe defender.
    
    Atributos:
        col (int): Columna inicial (9).
        fila (int): Fila inicial (última fila del mapa).
        ancho (int): Ancho en celdas (2).
        alto (int): Alto en celdas (1).
        vida_maxima (int): Vida máxima (100).
        vida (int): Vida actual.
    """

    def __init__(self, mapa: Mapa) -> None:
        """
        Inicializa la fogata y la marca en el mapa.
        
        Args:
            mapa: Referencia al mapa del juego.
        """
        self.col = COL_FOGATA
        self.fila = FILA_FOGATA
        self.ancho = ANCHO_FOGATA
        self.alto = ALTO_FOGATA
        self.vida_maxima = VIDA_MAXIMA
        self.vida = self.vida_maxima
        mapa.marcar_zona(self.col, self.fila, self.ancho, self.alto, CELDA_FOGATA)

    def esta_viva(self) -> bool:
        """
        Verifica si la fogata sigue en pie.
        
        Returns:
            bool: True si la vida es mayor a 0.
        """
        return self.vida > 0

    def porcentaje_vida(self) -> float:
        """
        Calcula el porcentaje de vida restante.
        
        Returns:
            float: Valor entre 0.0 y 1.0.
        """
        return self.vida / self.vida_maxima

    def recibir_dano(self, cantidad: int) -> None:
        """
        Reduce la vida de la fogata por una cantidad de daño.
        
        Args:
            cantidad: Puntos de daño a recibir.
            
        Raises:
            ValueError: Si la cantidad es negativa.
        """
        if cantidad < 0:
            raise ValueError(f"Daño negativo: {cantidad}")
        self.vida = max(0, self.vida - cantidad)