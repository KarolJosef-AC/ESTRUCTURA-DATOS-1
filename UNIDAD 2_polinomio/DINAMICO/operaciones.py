from class_polinomio import polinomio as PolinomioBase

class polinomio(PolinomioBase):
    # ─────────────────────────────────────────
    # OPERACIONES ALGEBRAICAS
    # ─────────────────────────────────────────

    def sumar(self, otro):
        """
        Ejecuta la suma algebraica lineal entre dos modelos polinómicos, agrupando
        y operando los términos que comparten el mismo grado.

        Parametros:
            otro (polinomio): La segunda estructura matemática a sumar.

        Retorna:
            polinomio: Una nueva entidad independiente que representa la adición
                       exacta de ambos sistemas.
        """
        if not isinstance(otro, polinomio):
            raise TypeError("Se esperaba un polinomio.")

        resultado = polinomio()
        for coef, exp in self.get_terminos():
            resultado.agregar_termino(coef, exp)
        for coef, exp in otro.get_terminos():
            resultado.agregar_termino(coef, exp)

        resultado.simplificar()
        return resultado

    def restar(self, otro):
        """
        Calcula la diferencia matemática entre dos polinomios. El proceso consiste
        en sumar al polinomio base el inverso aditivo de cada término del polinomio
        sustraendo.

        Parametros:
            otro (polinomio): El polinomio que actuará como sustraendo.

        Retorna:
            polinomio: Una nueva entidad que representa el resultado de la sustracción.
        """
        if not isinstance(otro, polinomio):
            raise TypeError("Se esperaba un polinomio.")

        resultado = polinomio()
        for coef, exp in self.get_terminos():
            resultado.agregar_termino(coef, exp)
        for coef, exp in otro.get_terminos():
            resultado.agregar_termino(-coef, exp)

        resultado.simplificar()
        return resultado

    def multiplicar(self, otro):
        """
        Calcula el producto polinómico expandido. Aplica la ley distributiva
        multiplicando cada coeficiente y sumando los exponentes correspondientes,
        según las leyes de los exponentes.

        Parametros:
            otro (polinomio): El polinomio multiplicador.

        Retorna:
            polinomio: Una nueva estructura resultante del producto cruzado completo.
        """
        if not isinstance(otro, polinomio):
            raise TypeError("Se esperaba un polinomio.")

        resultado = polinomio()
        for c1, e1 in self.get_terminos():
            for c2, e2 in otro.get_terminos():
                resultado.agregar_termino(c1 * c2, e1 + e2)

        resultado.simplificar()
        return resultado

    def dividir(self, otro):
        """
        Aplica el algoritmo clásico de división larga euclidiana para encontrar
        los polinomios cociente y residuo. Garantiza que el grado del residuo sea
        estrictamente inferior al grado del divisor.

        Parametros:
            otro (polinomio): El modelo matemático que actuará como divisor.

        Retorna:
            tuple: Una tupla compuesta por dos objetos de la clase polinomio
                   en el orden (cociente, residuo).
        """
        if otro.esta_vacio():
            raise ZeroDivisionError("No se puede dividir por el polinomio cero.")

        cociente = polinomio()
        residuo = polinomio()

        for coef, exp in self.get_terminos():
            residuo.agregar_termino(coef, exp)

        while (not residuo.esta_vacio() and residuo.get_grado() >= otro.get_grado()):
            coef_factor = residuo.get_coeficiente_lider() // otro.get_coeficiente_lider()
            exp_factor = residuo.get_grado() - otro.get_grado()

            if coef_factor != 0:
                cociente.agregar_termino(coef_factor, exp_factor)
            else:
                break

            for coef, exp in otro.get_terminos():
                residuo.agregar_termino(-coef_factor * coef, exp + exp_factor)

            residuo.simplificar()

        return cociente, residuo

    def evaluar(self, x):
        """
        Sustituye la variable independiente por una magnitud constante dada (x)
        para calcular el valor escalar neto de la expresión.

        Parametros:
            x (int): El escalar que reemplazará a la variable independiente.

        Retorna:
            int: La sumatoria de todos los términos evaluados en el punto x.
        """
        if not isinstance(x, int):
            raise TypeError("Solo se permiten valores enteros para x.")

        resultado = 0
        actual = self.cabeza
        while actual is not None:
            resultado += actual.coeficiente * (x ** actual.exponente)
            actual = actual.siguiente
        return resultado

    def derivar(self):
        """
        Ejecuta la operación de diferenciación sobre la estructura. De acuerdo con
        la regla de la potencia del cálculo diferencial, el exponente de cada término
        multiplica a la base, y el grado del término decrece en una unidad.

        Parametros:
            Ninguno.

        Retorna:
            polinomio: El modelo resultante tras aplicar la primera derivada formal.
        """
        resultado = polinomio()
        actual = self.cabeza
        while actual is not None:
            if actual.exponente > 0:
                resultado.agregar_termino(
                    actual.coeficiente * actual.exponente,
                    actual.exponente - 1
                )
            actual = actual.siguiente

        resultado.simplificar()
        return resultado