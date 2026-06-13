"""
Lista Enlazada - Inserción y eliminación dinámica.

Fase: 4 - Estructuras de datos manuales.
Cada nodo apunta al siguiente. Sin índices numéricos.
"""

class Nodo:
    """Un nodo de la lista. Guarda un dato y apunta al siguiente."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """Lista de nodos enlazados. Recorrible y modificable."""

    def __init__(self):
        self.cabeza = None
        self._tamano = 0

    def insertar(self, dato):
        """Inserta un dato al final de la lista."""
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamano += 1

    def eliminar(self, dato):
        """ Elimina el primer nodo que contenga el dato. True si lo encuentra"""
        if self.cabeza is None:
            return False
        
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self._tamano -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                self._tamano -= 1
            actual = actual.siguiente
        return False
    
    def recorrer(self):
        """ Devuelve una lista con todos los datos en orden"""
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def tamano(self):
        """Cantidad de nodos en la lista."""
        return self._tamano
    
    def vacia(self):
        """ True si tiene nodos"""
        return self.cabeza is None