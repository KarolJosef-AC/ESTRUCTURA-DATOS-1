"""
Listas de Comprensión y Filtrado

Transforma y filtra una secuencia de datos numéricos en una sola operación, reduciendo el tiempo de evaluación
"""
def filtrar_y_elevar_cuadrado(datos):
    """
    Filta los numeros pares de una lista y calcula su cuadrado matematico

    Parametros:
        datos (lista): SEcuencia original de valores numericos enteros.

    Retorna:
        lista: Nueva secuencia de valores resultantes tras aplicar la transformacion

    Nota de ejecucion:
        El proceso evalua la condicion de par (x % 2 == 0)
        a los elementos que cumplen la condicion, se les aplica la potencia (x ** 2)
    """

    datos_procesados = [valor ** 2 for valor in datos if valor % 2 == 0]

    return datos_procesados

if __name__ == "__main__":
      numeros_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      resultado_compresion = filtrar_y_elevar_cuadrado(numeros_base)
      print(resultado_compresion)