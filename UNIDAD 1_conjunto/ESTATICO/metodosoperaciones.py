from clase import ConjuntoEstatico as conjuntoEstatic

class ConjuntoEstatico(conjuntoEstatic):
    def union(self, otro):
        """
        Operación A ∪ B.

        La capacidad del resultado es la suma de ambas capacidades.

        Parametros:
            otro (ConjuntoEstatico): El conjunto B.

        Retorna:
            ConjuntoEstatico: Un nuevo conjunto con la unión.
        """
        capacidad = self.capacidad_maxima + otro.capacidad_maxima
        resultado = ConjuntoEstatico(capacidad, self.elementos)
        for elemento in otro.elementos:
            resultado.agregar(elemento)
        return resultado

    def interseccion(self, otro):
        """
        Operación A ∩ B.

        Parametros:
            otro (ConjuntoEstatico): El conjunto B.

        Retorna:
            ConjuntoEstatico: Un nuevo conjunto con la intersección.
        """
        capacidad = min(self.capacidad_maxima, otro.capacidad_maxima)
        resultado = ConjuntoEstatico(capacidad if capacidad > 0 else 1)
        for elemento in self.elementos:
            if elemento in otro.elementos:
                resultado.agregar(elemento)
        return resultado

    def diferencia(self, otro):
        """
        Operación A \\ B.

        Parametros:
            otro (ConjuntoEstatico): El conjunto B.

        Retorna:
            ConjuntoEstatico: Un nuevo conjunto con la diferencia.
        """
        resultado = ConjuntoEstatico(self.capacidad_maxima)
        for elemento in self.elementos:
            if elemento not in otro.elementos:
                resultado.agregar(elemento)
        return resultado

    def complemento(self, universal):
        """
        Operación A' respecto a U.

        Parametros:
            universal (ConjuntoEstatico): El conjunto universal U.

        Retorna:
            ConjuntoEstatico: Un nuevo conjunto con el complemento.
        """
        return universal.diferencia(self)

    def son_disjuntos(self, otro):
        """
        Verifica si A y B no comparten ningún elemento.

        Parametros:
            otro (ConjuntoEstatico): El conjunto B.

        Retorna:
            bool: True si A ∩ B = ∅, False si no.
        """
        return self.interseccion(otro).esta_vacio()