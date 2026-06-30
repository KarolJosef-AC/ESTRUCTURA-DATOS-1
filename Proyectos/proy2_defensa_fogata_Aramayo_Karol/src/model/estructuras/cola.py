"""
Cola (Queue) - FIFO: First In, First Out.
============================================
Fase: 4 - Estructuras de datos manuales.

El primer elemento que entra es el primero que sale.
Usada para gestionar las oleadas de enemigos.
"""


class Cola:
    """
    Cola FIFO implementada con lista simple.
    
    Garantiza que el orden de aparición de enemigos en el campo
    sea exactamente el orden en que fueron generados para la oleada.
    """

    def __init__(self):
        """Inicializa la cola vacía."""
        self._datos = []

    def encolar(self, enemigo):
        """
        Agrega un elemento al final de la cola.
        
        Args:
            enemigo: Enemigo a encolar.
        """
        self._datos.append(enemigo)

    def desencolar(self):
        """
        Saca y devuelve el primer elemento de la cola.
        
        Returns:
            El primer elemento encolado.
            
        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.vacia():
            raise IndexError("La cola esta vacia")
        return self._datos.pop(0)

    def frente(self):
        """
        Devuelve el primer elemento sin sacarlo.
        
        Returns:
            El primer elemento de la cola.
            
        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.vacia():
            raise IndexError("La cola esta vacia.")
        return self._datos[0]

    def vacia(self) -> bool:
        """
        Verifica si la cola está vacía.
        
        Returns:
            bool: True si no hay elementos.
        """
        return len(self._datos) == 0

    def tamano(self) -> int:
        """
        Cantidad de elementos en la cola.
        
        Returns:
            int: Número de elementos.
        """
        return len(self._datos)