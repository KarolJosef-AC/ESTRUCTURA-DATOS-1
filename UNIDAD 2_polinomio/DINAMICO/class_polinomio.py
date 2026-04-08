from nodo import NodoPolinomio

class polinomio:
    """
    Implementación de un Polinomio usando una lista enlazada.
    """
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        if coeficiente == 0:
            return

        nuevo = NodoPolinomio(coeficiente, exponente)

        if self.cabeza is None or exponente > self.cabeza.exponente:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual is not None:
            if actual.exponente == exponente:
                actual.coeficiente += coeficiente
                return
            if actual.siguiente is None or exponente > actual.siguiente.exponente:
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                return
            actual = actual.siguiente

    def get_cabeza(self):
        return self.cabeza

    def get_grado(self):
        if self.cabeza is None:
            return -1
        return self.cabeza.exponente

    def get_coeficiente_lider(self):
        if self.cabeza is None:
            return 0
        return self.cabeza.coeficiente

    def get_coeficiente(self, exponente):
        actual = self.cabeza
        while actual is not None:
            if actual.exponente == exponente:
                return actual.coeficiente
            actual = actual.siguiente
        return 0

    def get_terminos(self):
        terminos = []
        actual = self.cabeza
        while actual is not None:
            terminos.append((actual.coeficiente, actual.exponente))
            actual = actual.siguiente
        return terminos

    def esta_vacio(self):
        return self.cabeza is None

    def __str__(self):
        if self.esta_vacio():
            return "0"

        partes = []
        actual = self.cabeza
        while actual is not None:
            coef = actual.coeficiente
            expo = actual.exponente
            if expo == 0:
                partes.append(str(coef))
            elif expo == 1:
                partes.append(f"{coef}x^{expo}")
            else:
                partes.append(f"{coef}x^{expo}")
            actual = actual.siguiente

        return " + ".join(partes).replace("+ -", "- ")

    def simplificar(self):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.coeficiente == 0:
                if anterior is None:
                    self.cabeza = actual.siguiente
                    actual = self.cabeza
                else:
                    anterior.siguiente = actual.siguiente
                    actual = actual.siguiente
            else:
                anterior = actual
                actual = actual.siguiente