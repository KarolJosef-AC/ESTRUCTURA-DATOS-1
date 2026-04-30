from nodo import Nodo


class ListaSimpleEnlazada:
    """
    Estructura de Datos Dinámica: Lista Simple Enlazada.
    Incluye manejo de MemoryError para evitar desbordamientos.
    """

    def __init__(self):
        """
        Inicializa la lista en estado nulo.

        Parametros:
            Ninguno.

        Retorna:
            Ninguno. Establece los punteros cabecera y cola en None.
        """
        self.primero = None
        self.ultimo = None
        self._longitud = 0  

    def esta_vacia(self):
        """
        Verifica la condición de nulidad de la lista.

        Parametros:
            Ninguno.

        Retorna:
            bool: True si la lista carece de elementos, False en caso contrario.
        """
        return self.primero is None

    def get_longitud(self):
        """
        Obtiene la cantidad total de nodos actuales en la estructura.

        Parametros:
            Ninguno.

        Retorna:
            int: El número de elementos de la lista.
        """
        return self._longitud

    def get_primero(self):
        """
        Extrae el valor del nodo cabecera.

        Parametros:
            Ninguno.

        Retorna:
            Any: El dato del primer nodo, o None si la lista está vacía.
        """
        if self.esta_vacia():
            return None
        return self.primero.dato

    def get_ultimo(self):
        """
        Extrae el valor del nodo cola.

        Parametros:
            Ninguno.

        Retorna:
            Any: El dato del último nodo, o None si la lista está vacía.
        """
        if self.esta_vacia():
            return None
        return self.ultimo.dato

    def agregar_inicio(self, dato):
        """
        Incorpora un nuevo nodo al principio de la estructura.

        Valida que exista memoria RAM disponible en el sistema.

        Parametros:
            dato (Any): El valor a almacenar.

        Retorna:
            Ninguno. Modifica la estructura interna de punteros.
        """
        try:
            nuevo_nodo = Nodo(dato)
            if self.esta_vacia():
                self.primero = self.ultimo = nuevo_nodo
            else:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            self._longitud += 1

        except MemoryError:
            raise MemoryError("[OVERFLOW] Memoria RAM insuficiente.")

    def agregar_ultimo(self, dato):
        """
        Incorpora un nuevo nodo al final de la estructura.

        Gracias al puntero 'ultimo', esta operación es O(1).
        Valida que exista memoria RAM disponible en el sistema.

        Parametros:
            dato (Any): El valor a almacenar.

        Retorna:
            Ninguno.
        """
        try:
            nuevo_nodo = Nodo(dato)
            if self.esta_vacia():
                self.primero = self.ultimo = nuevo_nodo
            else:
                self.ultimo.siguiente = nuevo_nodo
                self.ultimo = nuevo_nodo
            self._longitud += 1

        except MemoryError:
            raise MemoryError("[OVERFLOW] Memoria RAM insuficiente.")

    def eliminar_inicio(self):
        """
        Desvincula y elimina el primer nodo de la lista.

        Valida previamente si la estructura contiene elementos para
        evitar un error de subdesbordamiento (Underflow).

        Parametros:
            Ninguno.

        Retorna:
            Ninguno. Muestra un mensaje de advertencia en consola si
            la lista está vacía.
        """
        if self.esta_vacia():
            return

        if self.primero is self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        
        self._longitud -= 1

    def eliminar_ultimo(self):
        """
        Elimina el nodo posicionado al final de la colección.

        Requiere recorrer secuencialmente los nodos hasta encontrar
        el penúltimo elemento para actualizar el puntero.

        Parametros:
            Ninguno.

        Retorna:
            Ninguno. Muestra un mensaje de advertencia en consola si
            la lista está vacía.
        """
        if self.esta_vacia():
            return

        if self.primero is self.ultimo:
            self.primero = self.ultimo = None
            self._longitud -= 1
            return

        actual = self.primero
        while actual.siguiente is not self.ultimo:
            actual = actual.siguiente
        
        actual.siguiente = None
        self.ultimo = actual
        self._longitud -= 1

    def recorrido(self):
        """
        Itera secuencialmente sobre la topología e imprime su estado
        para facilitar el análisis de escritorio y depuración.

        Parametros:
            Ninguno.

        Retorna:
            Ninguno. Imprime por consola.
        """
        print(f"\nEstado actual (Longitud: {self._longitud}):")
        actual = self.primero
        while actual is not None:
            print(f"[ {actual.dato} ]", end=" -> ")
            actual = actual.siguiente
        print("None")