"""
Defensa. Estructura que el jugador coloca para bloquear enemigos.
==================================================================
Fase: 5 - Construcciones defensivas.

Tipos de defensa:
- Valla: 40 HP, costo 20 oro. Solo bloquea.
- Torre: 30 HP, costo 50 oro. Dispara proyectiles.
- Muro: 80 HP, costo 30 oro. Mucha resistencia.
"""

from model.mapa import CELDA_OBSTACULO


class Defensa:
    """
    Una defensa colocada en el grid por el jugador.
    
    Atributos:
        col (int): Columna en el grid.
        fila (int): Fila en el grid.
        tipo (str): 'valla', 'torre' o 'muro'.
        vida (int): Vida actual.
        vida_max (int): Vida máxima.
        color (tuple): Color RGB para renderizado.
    """

    # Costos de cada tipo de defensa
    COSTOS = {
        "valla": 20,
        "torre": 50,
        "muro": 30
    }

    def __init__(self, col: int, fila: int, tipo: str = "valla"):
        """
        Inicializa una defensa según su tipo.
        
        Args:
            col: Columna donde se coloca.
            fila: Fila donde se coloca.
            tipo: 'valla', 'torre' o 'muro'.
        """
        self.col = col
        self.fila = fila
        self.tipo = tipo
        self._ultimo_disparo = 0.0

        if tipo == "valla":
            self.vida = 40
            self.color = (139, 90, 43)
        elif tipo == "torre":
            self.vida = 30
            self.color = (100, 100, 150)
        elif tipo == "muro":
            self.vida = 80
            self.color = (80, 80, 80)

        self.vida_max = self.vida

    def colocar_en_mapa(self, mapa) -> None:
        """
        Marca la celda como obstáculo en el mapa.
        
        Args:
            mapa: Referencia al mapa del juego.
        """
        mapa.poner(self.col, self.fila, CELDA_OBSTACULO)

    def puede_disparar(self, tiempo_actual: float) -> bool:
        """
        Verifica si la torre puede disparar según su tiempo de espera.        
        Args:
            tiempo_actual: Tiempo de juego actual.
            
        Returns:
            bool: True si puede disparar.
        """
        if self.tipo == "torre":
            tiempo_espera = 0.8

        # calcula el tiempo que paso desde el ultimo disparo
        timepo_transcurrido = tiempo_actual - self._ultimo_disparo

        # Paso tiempo suficiente?
        if timepo_transcurrido >= tiempo_espera:
            self._ultimo_disparo = tiempo_actual
            return True
        
        return False

    def recibir_dano(self, cantidad: int) -> None:
        """
        Reduce la vida de la defensa.
        
        Args:
            cantidad: Puntos de daño a recibir.
        """
        self.vida = max(0, self.vida - cantidad)

    def destruida(self) -> bool:
        """
        Verifica si la defensa fue destruida.
        
        Returns:
            bool: True si la vida llegó a 0.
        """
        return self.vida <= 0