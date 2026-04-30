class PolinomioArreglo:
    """
    Implementación de un Polinomio usando un arreglo (lista).

    El índice de cada posición representa el exponente y
    el valor en esa posición representa el coeficiente.

    Ejemplo:
        [3, 0, 2, 1] representa: 1x³ + 2x² + 0x + 3
    """

    def __init__(self, coeficientes=None):
        """
        Inicializa el polinomio.

        Parametros:
            coeficientes (list, optional): Lista de enteros donde
                el índice es el exponente. Si no se proporciona,
                se crea un polinomio vacío.

        Raises:
            TypeError: Si coeficientes no es una lista.
            TypeError: Si algún coeficiente no es entero.
        """
        if coeficientes is None:
            self.coeficientes = []
        else:
            # Se redujo a una sola validación fundamental
            if not isinstance(coeficientes, list):
                raise TypeError("Se esperaba una lista.")
            self.coeficientes = coeficientes

    # ─────────────────────────────────────────
    # GETTERS
    # ─────────────────────────────────────────

    def get_coeficiente(self, exponente):
        """
        Retorna el coeficiente de un exponente dado.

        Parametros:
            exponente (int): El exponente a consultar.

        Retorna:
            int: El coeficiente. Retorna 0 si el exponente
                 no existe en el polinomio.
        """
        if exponente >= len(self.coeficientes):
            return 0
        return self.coeficientes[exponente]

    def get_grado(self):
        """
        Retorna el grado del polinomio (mayor exponente
        con coeficiente distinto de cero).

        Retorna:
            int: El grado del polinomio. Retorna -1 si
                 el polinomio está vacío.
        """
        for i in range(len(self.coeficientes) - 1, -1, -1):
            if self.coeficientes[i] != 0:
                return i
        return -1

    def get_coeficiente_lider(self):
        """
        Retorna el coeficiente del término de mayor grado.

        Retorna:
            int: El coeficiente líder. Retorna 0 si el
                 polinomio está vacío.
        """
        grado = self.get_grado()
        if grado == -1:
            return 0
        return self.coeficientes[grado]

    def get_terminos(self):
        """
        Retorna una lista de tuplas (coeficiente, exponente)
        de los términos con coeficiente distinto de cero.

        Retorna:
            list: Lista de tuplas (coeficiente, exponente)
                  ordenada de mayor a menor exponente.
        """
        return [
            (self.coeficientes[i], i)
            for i in range(len(self.coeficientes) - 1, -1, -1)
            if self.coeficientes[i] != 0
        ]

    def esta_vacio(self):
        """
        Verifica si el polinomio no tiene términos.

        Retorna:
            bool: True si está vacío, False si no.
        """
        return self.get_grado() == -1

    def __str__(self):
        """
        Representación en cadena del polinomio.

        Retorna:
            str: El polinomio en notación matemática.
                 Ejemplo: 1x³ + 2x² + 3
        """
        terminos = self.get_terminos()
        if not terminos:
            return "0"

        partes = []
        for coef, exp in terminos:
            if exp == 0:
                partes.append(str(coef))
            elif exp == 1:
                partes.append(f"{coef}x")
            else:
                partes.append(f"{coef}x^{exp}")

        return " + ".join(partes).replace("+ -", "- ")
