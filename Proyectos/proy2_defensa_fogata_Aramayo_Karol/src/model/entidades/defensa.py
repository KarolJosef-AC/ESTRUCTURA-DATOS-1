"""
Defensa. Estructura que el jugador coloca para bloquear enemigos.

Fase: 5 - Construcciones defensivas.
"""

from model.mapa import  CELDA_OBSTACULO

class Defensa:
    """ Una defensa colocada en el grid."""

    def __init__(self, col:int, fila:int, tipo: str = "valla"):
        """
        Args:
            col: columna en el grid.
            fila: fila en el grid.
            tipo: "valla", "torre", "muro".
        """
        self.col = col
        self.fila = fila
        self.tipo = tipo

        if tipo == "valla":
            self.vida = 40
            self.color = (130, 90, 43)
        elif tipo == "torre":
            self.vida = 30
            self.color = (100, 100, 150)
        elif tipo == "muro":
            self.vida = 80
            self.color = (80, 80, 80)
        self.vida_max = self.vida

    # FASE 6 - Metodo para disparar
    def puede_disparar(self, tiempo_actual: float) -> bool:
        """ True si paso suficiente tiempo desde el ultimo disparo"""
        if not hasattr(self, '_ultimo disparo'):
            self._ultimo_disparo = 0.0

        intervalo = 1.0
        if self.tipo == "torre":
            intervalo = 0.8

        if tiempo_actual - self._ultimo_disparo >= intervalo:
            self._ultimo_disparo = tiempo_actual
            return True
        return False
    ## FIN FASE 6
    
    def colocar_en_mapa(self, mapa) -> None:
        """Marca la celda como obstaculo en el mapa."""
        mapa.poner = (self.col, self.fila,CELDA_OBSTACULO)

    def recibir_dano(self, cantidad:int) -> None:
        """Reduce la vida de la defensa."""
        self.vida = max(0, self.vida - cantidad)

    def destruido(self) -> bool:
        """True si la defensa ya no tiene vida. """
        return self.vida <= 0