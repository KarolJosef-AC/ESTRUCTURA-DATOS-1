"""
Enemigo. Criatura que avanza hacia la fogata.
===============================================
Fase: 3 - Movimiento de enemigos.

Cada enemigo es un "proceso" con tiempo de ejecución medible:
- ESPERANDO: En la cola de oleadas.
- ACTIVO: Bajando hacia la fogata.
- TERMINADO: Murió o llegó a la fogata.
"""

from model.mapa import TAM_CELDA


class Enemigo:
    """
    Un enemigo que baja desde la parte superior hacia la fogata.
    
    Atributos:
        col (int): Columna actual en el grid.
        fila (int): Fila actual en el grid.
        tipo (str): 'normal' o 'tanque'.
        vida (int): Vida actual.
        vida_max (int): Vida máxima.
        velocidad (float): Velocidad de avance.
        color (tuple): Color RGB para renderizado.
        x (float): Posición x en píxeles.
        y (float): Posición y en píxeles.
        tiempo_salida (float): Momento en que salió de la cola (inicio de ejecución).
    """

    def __init__(self, col: int, fila: int, tipo: str = 'normal'):
        """
        Inicializa un enemigo con sus atributos según el tipo.
        
        Args:
            col: Columna inicial.
            fila: Fila inicial.
            tipo: 'normal' (45 HP, rápido) o 'tanque' (80 HP, lento) o "rapido" (25 HP, rapido).
        """
        self.col = col
        self.fila = fila
        self.tipo = tipo

        if tipo == 'normal':
            self.vida = 45
            self.vida_max = 45
            self.velocidad = 0.8
            self.color = (180, 40, 40)
        elif tipo == 'tanque':
            self.vida = 80
            self.vida_max = 80
            self.velocidad = 0.6
            self.color = (100, 40, 100)
        elif tipo == "rapido":
            self.vida = 25
            self.vida_max = 25
            self.velocidad = 1.4
            self.color = (128, 0, 128)

        self.x = col * TAM_CELDA
        self.y = fila * TAM_CELDA
        self._acumulado = 0.0
        self._direccion = 1
        
        # Atributo para el planificador: mide el tiempo de ejecución del proceso
        self.tiempo_salida = 0.0

    def mover(self, dt: float, mapa) -> bool:
        """
        Avanza el enemigo hacia abajo. Si encuentra un obstáculo,
        intenta esquivarlo (solo tipo 'normal').
        
        Args:
            dt: Delta time desde el último frame.
            mapa: Referencia al mapa del juego.
            
        Returns:
            bool: True si el enemigo llegó al final del mapa (fogata).
        """
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

            if not mapa.libre(self.col, nueva_fila):
                if self.tipo == 'tanque':
                    return False
                elif self.tipo == 'normal':
                    for _ in range(2):
                        nueva_col = self.col + self._direccion
                        if mapa.dentro(nueva_col, self.fila) and mapa.libre(nueva_col, self.fila):
                            self.col = nueva_col
                            self._sincronizar_pixeles()
                            return False
                        self._direccion *= -1
                    if self.fila > 0 and mapa.libre(self.col, self.fila - 1):
                        self.fila -= 1
                        self.y = self.fila * TAM_CELDA
                    return False

            self.fila = nueva_fila
            self._sincronizar_pixeles()

        return False

    def recibir_dano(self, cantidad: int) -> None:
        """
        Reduce la vida del enemigo.
        
        Args:
            cantidad: Puntos de daño a recibir.
        """
        self.vida = max(0, self.vida - cantidad)

    def esta_vivo(self) -> bool:
        """
        Verifica si el enemigo sigue con vida.
        
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
        return self.vida / self.vida_max
    
    def _sincronizar_pixeles(self) -> None:
        """Actualiza las coordenadas x, y desde col, fila."""
        self.x = self.col * TAM_CELDA
        self.y = self.fila * TAM_CELDA