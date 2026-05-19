from nodo import Nodo

class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0
    
    def apilar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo
        self.tamanio += 1
        print(f"Apilado: {dato}")
    
    def desapilar(self):
        if self.cima is None:
            print("Pila vacia")
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        self.tamanio -= 1
        print(f"Desapilado: {dato}")
        return dato
    
    def ver_cima(self):
        if self.cima is None:
            return None
        return self.cima.dato
    
    def esta_vacia(self):
        return self.cima is None
    
    def tamaño(self):
        return self.tamanio
    
    def mostrar(self):
        if self.cima is None:
            print("Pila vacia")
            return
        actual = self.cima
        print("Pila:")
        while actual:
            print(f"  {actual.dato}")
            actual = actual.siguiente