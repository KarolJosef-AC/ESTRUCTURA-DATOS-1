"""
Cola (Queue) - FIFO: First In, First Out.

Fase: 4 - Estructuras de datos manuales.
El primero que entra es el primero que sale.
"""

class Cola:
    """ Cola implementada con lista simple."""

    def __init__(self):
        self._datos = []

    def encolar(self, enemigo):
        """Agrega un elemento al final de la cola."""
        self._datos.append(enemigo)

    def desencolar(self):
        """ 
        Saca y devuelve el primer elemento.
        lanza IndexError si esta vacia
        """
        if self.vacia():
            raise IndexError("La cola esta vacia")
        return self._datos.pop(0)
    
    def frente(self):
        if self.vacia():
            raise IndexError("La cola esta vacia.")
        return self._datos[0]
    
    def vacia(self):
        """True si la cola no tiene elemnento"""
        return len(self._datos) == 0
    
    def tamano(self):
        """Cantidad de elementos de la cola"""
        return len(self._datos)