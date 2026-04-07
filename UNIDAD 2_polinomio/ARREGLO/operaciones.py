from clase import PolinomioArreglo as pArreglo

class PolinomioArreglo(pArreglo):

  def sumar(self, otro):
        """
        Suma dos polinomios A + B.

        Parametros:
            otro (PolinomioArreglo): El polinomio B.

        Retorna:
            PolinomioArreglo: Un nuevo polinomio con la suma.

        Raises:
            TypeError: Si otro no es un PolinomioArreglo.
        """
        if not isinstance(otro, PolinomioArreglo):
            raise TypeError("Se esperaba un PolinomioArreglo.")

        longitud = max(len(self.coeficientes), len(otro.coeficientes))
        resultado = []
        for i in range(longitud):
            resultado.append(self.get_coeficiente(i) + otro.get_coeficiente(i))
        return PolinomioArreglo(resultado)

  def restar(self, otro):
        """
        Resta dos polinomios A - B.

        Parametros:
            otro (PolinomioArreglo): El polinomio B.

        Retorna:
            PolinomioArreglo: Un nuevo polinomio con la resta.

        Raises:
            TypeError: Si otro no es un PolinomioArreglo.
        """
        if not isinstance(otro, PolinomioArreglo):
            raise TypeError("Se esperaba un PolinomioArreglo.")

        longitud = max(len(self.coeficientes), len(otro.coeficientes))
        resultado = []
        for i in range(longitud):
            resultado.append(self.get_coeficiente(i) - otro.get_coeficiente(i))
        return PolinomioArreglo(resultado)

  def multiplicar(self, otro):
        """
        Multiplica dos polinomios A * B.

        Parametros:
            otro (PolinomioArreglo): El polinomio B.

        Retorna:
            PolinomioArreglo: Un nuevo polinomio con el producto.

        Raises:
            TypeError: Si otro no es un PolinomioArreglo.
        """
        if not isinstance(otro, PolinomioArreglo):
            raise TypeError("Se esperaba un PolinomioArreglo.")

        grado_resultado = self.get_grado() + otro.get_grado()
        resultado = [0] * (grado_resultado + 1)
        for i, c1 in enumerate(self.coeficientes):
            for j, c2 in enumerate(otro.coeficientes):
                resultado[i + j] += c1 * c2
        return PolinomioArreglo(resultado)

  def dividir(self, otro):
        """
        Divide dos polinomios A / B usando división larga.

        Parametros:
            otro (PolinomioArreglo): El divisor B.

        Retorna:
            tuple: (cociente, residuo) ambos PolinomioArreglo.

        Raises:
            TypeError: Si otro no es un PolinomioArreglo.
            ZeroDivisionError: Si el divisor es el polinomio cero.
        """
        if otro.esta_vacio():
            raise ZeroDivisionError("No se puede dividir por el polinomio cero.")

        dividendo = list(self.coeficientes)
        divisor = otro.coeficientes
        grado_div = otro.get_grado()
        cociente = [0] * (len(dividendo))

        for i in range(len(dividendo) - 1, grado_div - 1, -1):
            if divisor[grado_div] == 0:
                continue
            factor = dividendo[i] // divisor[grado_div]
            cociente[i - grado_div] = factor
            for j in range(grado_div + 1):
                dividendo[i - grado_div + j] -= factor * divisor[j]

        residuo = PolinomioArreglo(dividendo[:grado_div])
        return PolinomioArreglo(cociente), residuo

  def evaluar(self, x):
        """
        Evalúa el polinomio en un punto dado usando la
        regla de Horner.

        Parametros:
            x (int): El valor en el que se evalúa el polinomio.

        Retorna:
            int: El resultado de evaluar el polinomio en x.

        Raises:
            TypeError: Si x no es un entero.
        """
        if not isinstance(x, int):
            raise TypeError("Solo se permiten valores enteros para x.")

        resultado = 0
        for i in range(len(self.coeficientes) - 1, -1, -1):
            resultado = resultado * x + self.coeficientes[i]
        return resultado

  def derivar(self):
        """
        Calcula la derivada del polinomio.

        Retorna:
            PolinomioArreglo: Un nuevo polinomio con la derivada.
        """
        if len(self.coeficientes) <= 1:
            return PolinomioArreglo([0])
        resultado = []
        for i in range(1, len(self.coeficientes)):
            resultado.append(i * self.coeficientes[i])
        return PolinomioArreglo(resultado)