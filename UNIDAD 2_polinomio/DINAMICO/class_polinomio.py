from nodo import NodoPolinomio

class polinomio:
    """
    Implementación de un Polinomio usando una lista enlazada.

    Cada nodo representa un término algebraico definido por un escalar (coeficiente)
    y una potencia (exponente). La topología se mantiene ordenada de forma estricta
    de mayor a menor exponente, garantizando que el nodo cabecera contenga siempre
    el término que dicta el grado del polinomio.
    """

    def __init__(self):
        """
        Inicializa la estructura del polinomio en un estado nulo.

        Parametros:
            Ninguno.

        Retorna:
            Ninguno. Establece la cabeza de la secuencia topológica como vacía.
        """
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        """
        Incorpora un nuevo término algebraico al modelo matemático, preservando
        el orden descendente de los exponentes. Si se introduce un término con
        un exponente ya existente, aplica el principio de superposición, sumando
        algebraicamente sus coeficientes.

        Parametros:
            coeficiente (int): El valor escalar que multiplica a la variable.
            exponente (int): La potencia a la que está elevada la variable.

        Retorna:
            Ninguno. Modifica la estructura interna del objeto.
        """
        # Evitamos inyectar masa nula al sistema desde el principio
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

    # ─────────────────────────────────────────
    # GETTERS (Propiedades de Observación)
    # ─────────────────────────────────────────

    def get_cabeza(self):
        """
        Extrae el nodo fundamental de la estructura enlazada, que representa
        el término de mayor jerarquía en la ecuación.

        Parametros:
            Ninguno.

        Retorna:
            NodoPolinomio: La entidad que contiene el término de mayor grado,
                           o None si el polinomio carece de términos.
        """
        return self.cabeza

    def get_grado(self):
        """
        Evalúa el grado absoluto del polinomio, que corresponde matemáticamente
        al exponente de mayor magnitud en toda la expresión.

        Parametros:
            Ninguno.

        Retorna:
            int: El grado máximo. Si el polinomio es el polinomio nulo,
                 retorna -1 por convención matemática estándar.
        """
        if self.cabeza is None:
            return -1
        return self.cabeza.exponente

    def get_coeficiente_lider(self):
        """
        Identifica el coeficiente principal de la expresión matemática. Es el
        escalar asociado a la variable de mayor exponente.

        Parametros:
            Ninguno.

        Retorna:
            int: El valor numérico del coeficiente líder. Retorna 0 si el
                 modelo está vacío.
        """
        if self.cabeza is None:
            return 0
        return self.cabeza.coeficiente

    def get_coeficiente(self, exponente):
        """
        Localiza el escalar específico que acompaña a una potencia particular
        dentro de la serie del polinomio.

        Parametros:
            exponente (int): El grado del término a consultar.

        Retorna:
            int: El coeficiente encontrado. Si el grado no existe en la ecuación,
                 se deduce que el término es nulo y retorna 0.
        """
        actual = self.cabeza
        while actual is not None:
            if actual.exponente == exponente:
                return actual.coeficiente
            actual = actual.siguiente
        return 0

    def get_terminos(self):
        """
        Proyecta la estructura enlazada en una lista secuencial de coordenadas
        bidimensionales, facilitando su análisis externo.

        Parametros:
            Ninguno.

        Retorna:
            list: Una colección de tuplas ordenadas bajo el formato
                  (coeficiente, exponente).
        """
        terminos = []
        actual = self.cabeza
        while actual is not None:
            terminos.append((actual.coeficiente, actual.exponente))
            actual = actual.siguiente
        return terminos

    def esta_vacio(self):
        """
        Verifica la condición de nulidad del sistema algebraico.

        Parametros:
            Ninguno.

        Retorna:
            bool: True si la ecuación es P(x) = 0 (no contiene nodos),
                  False en caso contrario.
        """
        return self.cabeza is None

    def __str__(self):
        """
        Construye la representación simbólica de la ecuación matemática,
        transformando los datos estructurales en una sintaxis legible para
        el análisis humano.

        Parametros:
            Ninguno.

        Retorna:
            str: Una cadena de texto que ilustra el polinomio formal
                 (ejemplo: "4x^3 - 2x^2 + 7").
        """
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

    # ─────────────────────────────────────────
    # CONTRACCIÓN TOPOLÓGICA (Prevención de Bucles)
    # ─────────────────────────────────────────

    def simplificar(self):
        """
        Escanea la ecuación y desintegra cualquier término cuyo coeficiente
        haya colapsado a cero tras una operación matemática, asegurando
        que el grado del polinomio sea siempre preciso.

        Parametros:
            Ninguno.

        Retorna:
            Ninguno. Modifica la estructura interna eliminando nodos nulos.
        """
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