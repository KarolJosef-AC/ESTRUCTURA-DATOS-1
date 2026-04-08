class Nodo:
    """
    Almacena el valor de la información y mantiene la topología 
    de la estructura mediante un puntero al siguiente elemento.
    """
    def __init__(self, dato):
        """
        Inicializa un nodo aislado en memoria.

        Parametros:
            dato (Any): El valor o información que almacenará el nodo.

        Retorna:
            Ninguno.
        """
        self.dato = dato
        self.siguiente = None
