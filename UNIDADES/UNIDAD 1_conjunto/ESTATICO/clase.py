class ConjuntoEstatico:
    """
    Implementación de un Conjunto matemático estático.

    Cumple con el axioma de extensionalidad: no permite
    elementos duplicados. Su capacidad máxima se define
    al momento de la creación y no puede modificarse.
    """

    def __init__(self, capacidad_maxima, elementos_iniciales=None):
        """
        Inicializa el conjunto estático.

        Parametros:
            capacidad_maxima (int): Límite máximo de elementos.
            elementos_iniciales (iterable, optional): Elementos
                con los que se construye el conjunto. Los
                duplicados son ignorados automáticamente.

        Raises:
            TypeError: Si capacidad_maxima no es un entero positivo.
            OverflowError: Si los elementos iniciales superan la capacidad.
        """
        if not isinstance(capacidad_maxima, int) or capacidad_maxima <= 0:
            raise TypeError(
                f"La capacidad debe ser un entero positivo. "
                f"Se recibió: {capacidad_maxima!r}."
            )

        self.capacidad_maxima = capacidad_maxima
        self.elementos = []

        if elementos_iniciales is not None:
            for elemento in elementos_iniciales:
                self.agregar(elemento)

    def agregar(self, elemento):
        """
        Añade un elemento respetando la capacidad máxima.

        Parametros:
            elemento (int): El elemento a agregar.

        Raises:
            TypeError: Si el elemento no es un entero.
            OverflowError: Si el conjunto ya alcanzó su capacidad.
        """
        if not isinstance(elemento, int):
            raise TypeError(
                f"Solo se permiten enteros. "
                f"Se recibió '{type(elemento).__name__}': {elemento!r}."
            )
        if len(self.elementos) >= self.capacidad_maxima:
            raise OverflowError(
                f"Conjunto lleno. Capacidad máxima: {self.capacidad_maxima}."
            )
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def esta_lleno(self):
        """
        Verifica si el conjunto alcanzó su capacidad máxima.

        Retorna:
            bool: True si está lleno, False si no.
        """
        return len(self.elementos) == self.capacidad_maxima

    def esta_vacio(self):
        """
        Verifica si el conjunto no tiene elementos.

        Retorna:
            bool: True si está vacío, False si no.
        """
        return len(self.elementos) == 0

    def __len__(self):
        """
        Retorna la cardinalidad del conjunto.

        Retorna:
            int: Número de elementos en el conjunto.
        """
        return len(self.elementos)

    def __contains__(self, elemento):
        """
        Permite usar el operador 'in' directamente.

        Parametros:
            elemento (int): El elemento a buscar.

        Retorna:
            bool: True si el elemento pertenece al conjunto.
        """
        return elemento in self.elementos

    def __eq__(self, otro):
        """
        Permite usar el operador '==' directamente.

        Parametros:
            otro (ConjuntoEstatico): El conjunto a comparar.

        Retorna:
            bool: True si ambos conjuntos tienen los mismos elementos.
        """
        if not isinstance(otro, ConjuntoEstatico):
            return False
        return sorted(self.elementos) == sorted(otro.elementos)

    def __str__(self):
        """
        Representación en cadena con notación matemática.

        Retorna:
            str: El conjunto con formato {a, b, c}
                 o '∅' si está vacío.
        """
        if self.esta_vacio():
            return "∅"
        elementos_str = ", ".join(str(e) for e in self.elementos)
        return f"{{{elementos_str}}}"