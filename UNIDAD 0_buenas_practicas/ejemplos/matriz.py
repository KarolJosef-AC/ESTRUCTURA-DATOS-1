"""
Creacion de una Matriz

El algoritmo utiliza bucles anidados para construir una estructura de "lista de listas"

"""


def crear_matriz(filas, columnas):
    """
    Genera una matriz con una secuencia numérica continua del 1 al n.

    Parametros:
        filas (entero): Numero de filas de la matriz.
        columnas (entero): Numero de columnas de la matriz

    Retorna:
        lista: Una lista de listas representando la matriz
    """
    matriz = []
    contador = 1
    for _ in range(filas):
        fila_temporal = []
        for y in range(columnas):
            fila_temporal.append(contador)
            contador += 1
        matriz.append(fila_temporal)
    return matriz

if __name__ == "__main__":
    mi_matriz = crear_matriz(3, 3)
    for fila in mi_matriz:
        print(fila)