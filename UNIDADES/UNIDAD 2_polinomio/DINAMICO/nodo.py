class NodoPolinomio:
    """
    Nodo de la lista enlazada que representa un término
    del polinomio.

    Cada nodo almacena un coeficiente, su exponente
    y una referencia al siguiente nodo.
    """

    def __init__(self, coeficiente, exponente):
        """
        Inicializa el nodo.

        Parametros:
            coeficiente (int): El coeficiente del término.
            exponente (int): El exponente del término.

        Raises:
            ValueError: Si el exponente no es válido matemáticamente.
        """
        if not isinstance(exponente, int) or exponente < 0:
            raise ValueError("El exponente debe ser un entero no negativo")

        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None