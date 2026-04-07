"""

Busqueda Binaria


"""
lista_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def busqueda_binaria(dato, lista):
    """
    Ejecuta un algoritmo de búsqueda logarítmica sobre una lista ordenada.

    Parameters:
        dato (entero): El valor numérico a localizar.
        lista (lista): La estructura de datos secuencial ordenada.

    Returns:
        entero o None: El índice de la posición del dato, o None si es inexistente.
    """
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if dato == lista[medio]:
            return medio
        elif dato < lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1

def buscar(dato):
    """
    Evalúa el retorno de la búsqueda y estructura el mensaje final.
    """
    resultado = busqueda_binaria(dato, lista_base)

    if resultado is None:
        return f"El dato {dato} no se encontro en la lista"
    else:
        return f"El dato {dato} se encontro en el indice {resultado}"

if __name__ == "__main__":
    dato_usuario = int(input("Ingrese un dato numerico:"))
    resultado_final = buscar(dato_usuario)
    print(resultado_final)
