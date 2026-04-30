from  clase import  ConjuntoPersistente as cPersistente



class ConjuntoPersistente(cPersistente):

    def union(self, otro):
        """
        Operación A ∪ B.

        El resultado se guarda en un archivo temporal.

        Parametros:
            otro (ConjuntoPersistente): El conjunto B.

        Retorna:
            ConjuntoPersistente: Un nuevo conjunto con la unión.
        """
        resultado = ConjuntoPersistente("_temp_union", self.elementos)
        for elemento in otro.elementos:
            resultado.agregar(elemento)
        return resultado

    def interseccion(self, otro):
        """
        Operación A ∩ B.

        Parametros:
            otro (ConjuntoPersistente): El conjunto B.

        Retorna:
            ConjuntoPersistente: Un nuevo conjunto con la intersección.
        """
        resultado = ConjuntoPersistente("_temp_interseccion")
        for elemento in self.elementos:
            if elemento in otro.elementos:
                resultado.agregar(elemento)
        return resultado

    def diferencia(self, otro):
        """
        Operación A \\ B.

        Parametros:
            otro (ConjuntoPersistente): El conjunto B.

        Retorna:
            ConjuntoPersistente: Un nuevo conjunto con la diferencia.
        """
        resultado = ConjuntoPersistente("_temp_diferencia")
        for elemento in self.elementos:
            if elemento not in otro.elementos:
                resultado.agregar(elemento)
        return resultado

    def complemento(self, universal):
        """
        Operación A' respecto a U.

        Parametros:
            universal (ConjuntoPersistente): El conjunto universal U.

        Retorna:
            ConjuntoPersistente: Un nuevo conjunto con el complemento.
        """
        return universal.diferencia(self)

    def son_disjuntos(self, otro):
        """
        Verifica si A y B no comparten ningún elemento.

        Parametros:
            otro (ConjuntoPersistente): El conjunto B.

        Retorna:
            bool: True si A ∩ B = ∅, False si no.
        """
        return self.interseccion(otro).esta_vacio()