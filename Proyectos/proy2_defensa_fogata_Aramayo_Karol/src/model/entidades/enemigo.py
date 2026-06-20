"""
Enemigo. Criatura que avanza hacia la fogata.

Fase: 3 - Movimiento de enemigos.
"""

from model.mapa import TAM_CELDA

class Enemigo:
    """Un enemigo que baja desde arriba hacia la fogata."""
    def __init__(self, col: int, fila:int, tipo: str = 'normal'):
        self.col = col
        self.fila = fila
        self.tipo = tipo

        if tipo == 'normal':
            self.vida = 30
            self.vida_max = 30
            self.velocidad = 0.6
            self.color = (180, 40, 40)
        elif tipo == 'tanque':
            self.vida = 80
            self.vida_max = 80
            self.velocidad = 0.3
            self.color = (100, 40, 100)

        self.x = col * TAM_CELDA
        self.y = fila * TAM_CELDA
        self._acumulado = 0.0
        self._direccion = 1

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

            # Verificar si la celda de abajo esta bloqueada
            if not mapa.libre(self.col, nueva_fila):
                if self.tipo == 'tanque':
                    return False # se queda -> controlador maneja daño
                elif self.tipo == 'normal':
                    for _ in range(2):
                        nueva_col = self.col + self._direccion
                        if mapa.dentro(nueva_col, self.fila) and mapa.libre(nueva_col, self.fila):
                            self.col = nueva_col
                            self.x = self.col * TAM_CELDA
                            return False
                        self._direccion *= -1
                    if self.fila > 0 and mapa.libre(self.col, self.fila -1):
                        self.fila -= -1
                        self.y = self.fila * TAM_CELDA
                    return False
                
            self.fila = nueva_fila
            self.y = self.fila * TAM_CELDA

        return False
    
    def recibir_dano(self, cantidad:int ) -> None:
        self.vida = max(0, self.vida - cantidad)

    def esta_vivo(self) -> bool:
        return self.vida > 0
    
    def porcentaje_vida(self) -> float:
        return self.vida / self.vida_max
