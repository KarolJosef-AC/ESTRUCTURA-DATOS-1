class Conjunto:
    """
    Implementación de un Conjunto matemático.

    Cumple con el axioma de extensionalidad: no permite
    elementos duplicados. Soporta las operaciones clásicas
    de la teoría de conjuntos.
    """
    def __init__(self, elementos_iniciales=None):
        """
        Inicializa el conjunto.

        Parametros:
            elementos_iniciales (iterable, optional): Elementos
                con los que se construye el conjunto. Los
                duplicados son ignorados automáticamente.
        """
        self.elementos = []

        if elementos_iniciales is not None:
            for elemento in elementos_iniciales:
                self.agregar(elemento)

    def agregar(self, elemento):
        """
        Añade un elemento al conjunto.

        Valida el axioma de extensionalidad: si el elemento
        ya existe, no se agrega.

        Parametros:
            elemento: El elemento a agregar.
        """
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def __len__(self):
        """
        Retorna la cardinalidad del conjunto.

        Retorna:
            int: Número de elementos en el conjunto.
        """
        return len(self.elementos)

    def __str__(self):
        """
        Representación en cadena con notación matemática.

        Retorna:
            str: El conjunto con formato {a, b, c}.
        """
        elementos_str = ", ".join(str(e) for e in self.elementos)
        return f"{{{elementos_str}}}"