from nodo import Nodo

class Cola:
    """Estructura de datos FIFO (First In, First Out) implementada con nodos enlazados."""
    
    def __init__(self):
        """Inicializa una cola vacía."""
        self.frente = None
        self.final = None
        self.tamanio = 0
    
    def encolar(self, dato):
        """
        Agrega un elemento al final de la cola.
        
        Args:
            dato: El elemento a agregar.
        """
        nuevo = Nodo(dato)
        if self.final is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamanio += 1
        print(f"Encolado: {dato}")
    
    def desencolar(self):
        """
        Quita y devuelve el elemento del frente de la cola.
        
        Returns:
            El elemento del frente, o None si la cola está vacía.
        """
        if self.frente is None:
            print("Cola vacia")
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamanio -= 1
        print(f"Desencolado: {dato}")
        return dato
    
    def ver_frente(self):
        """
        Devuelve el elemento del frente sin quitarlo.
        
        Returns:
            El elemento del frente, o None si la cola está vacía.
        """
        if self.frente is None:
            return None
        return self.frente.dato
    
    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        
        Returns:
            True si la cola está vacía, False en caso contrario.
        """
        return self.frente is None
    
    def obtener_tamanio(self):
        """
        Devuelve la cantidad de elementos en la cola.
        
        Returns:
            Número entero de elementos.
        """
        return self.tamanio
    
    def mostrar(self):
        """Muestra todos los elementos de la cola desde el frente hasta el final."""
        if self.frente is None:
            print("Cola vacia")
            return
        actual = self.frente
        print("Cola (frente -> final):")
        while actual:
            print(f"  {actual.dato}")
            actual = actual.siguiente