from clase import Conjunto as conjuntoBase

class Conjunto(conjuntoBase):
    def union(self, otro_conjunto):
        """
        Operación A ∪ B.

        Retorna un nuevo Conjunto con todos los elementos
        de A y de B, sin duplicados.

        Parametros:
            otro_conjunto (Conjunto): El conjunto B.

        Retorna:
            Conjunto: Un nuevo conjunto con la unión.
        """
        resultado = Conjunto(self.elementos)
        for elemento in otro_conjunto.elementos:
            resultado.agregar(elemento)
        return resultado

    def interseccion(self, otro_conjunto):
        """
        Operación A ∩ B.

        Retorna un nuevo Conjunto con los elementos que
        están en A y también en B.

        Parametros:
            otro_conjunto (Conjunto): El conjunto B.

        Retorna:
            Conjunto: Un nuevo conjunto con la intersección.
        """
        resultado = Conjunto()
        for elemento in self.elementos:
            if elemento in otro_conjunto.elementos:
                resultado.agregar(elemento)
        return resultado

    def diferencia(self, otro_conjunto):
        """
        Operación A \\ B.

        Retorna un nuevo Conjunto con los elementos que
        están en A pero NO en B.

        Parametros:
            otro_conjunto (Conjunto): El conjunto B.

        Retorna:
            Conjunto: Un nuevo conjunto con la diferencia.
        """
        resultado = Conjunto()
        for elemento in self.elementos:
            if elemento not in otro_conjunto.elementos:
                resultado.agregar(elemento)
        return resultado

    def diferencia_simetrica(self, otro_conjunto):
        """
        Operación A △ B.

        Retorna un nuevo Conjunto con los elementos que
        están en A o en B, pero NO en ambos.

        Parametros:
            otro_conjunto (Conjunto): El conjunto B.

        Retorna:
            Conjunto: Un nuevo conjunto con la diferencia simétrica.
        """
        return self.union(otro_conjunto).diferencia(
            self.interseccion(otro_conjunto)
        )
    def eliminar(self, elemento):
            """
            Elimina un elemento del conjunto.

            Parametros:
                elemento (int): El elemento a eliminar.

            Retorna:
                KeyError: Si el elemento no existe en el conjunto.
            """
            if elemento not in self.elementos:
                raise KeyError(
                    f"El elemento {elemento!r} no existe en el conjunto."
                )
            self.elementos.remove(elemento)