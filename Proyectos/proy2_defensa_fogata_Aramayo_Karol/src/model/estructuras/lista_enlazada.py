"""
Lista Enlazada - Inserción y eliminación dinámica.
====================================================
Fase: 4 - Estructuras de datos manuales.

Cada nodo apunta al siguiente. Sin índices numéricos.
Ventaja: eliminación O(1) de cualquier posición sin reindexar.
Usada para gestionar los enemigos activos en el campo.
"""


class Nodo:
    """
    Un nodo de la lista enlazada.
    
    Atributos:
        dato: El elemento almacenado.
        siguiente: Referencia al siguiente nodo.
    """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """
    Lista de nodos enlazados. Recorrible y modificable.
    
    Usada para enemigos activos porque permite eliminar
    enemigos en cualquier posición sin reindexar (O(1)).
    """

    def __init__(self):
        """Inicializa la lista vacía."""
        self.cabeza = None
        self._tamano = 0

    def insertar(self, dato):
        """
        Inserta un dato al final de la lista.
        
        Args:
            dato: Elemento a insertar.
        """
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamano += 1

    def eliminar(self, dato) -> bool:
        """
        Elimina el primer nodo que contenga el dato.
        
        Args:
            dato: Elemento a eliminar.
            
        Returns:
            bool: True si lo encontró y eliminó.
        """
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
                return True
            actual = actual.siguiente

        return False

    def recorrer(self) -> list:
        """
        Devuelve una lista con todos los datos en orden.
        
        Returns:
            list: Lista con los elementos en orden.
        """
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def tamano(self) -> int:
        """
        Cantidad de nodos en la lista.
        
        Returns:
            int: Número de nodos.
        """
        return self._tamano

    def vacia(self) -> bool:
        """
        Verifica si la lista está vacía.
        
        Returns:
            bool: True si no tiene nodos.
        """
        return self.cabeza is None