"""

Factorial de n - Recursivo

Implementacion recursiva de la recurrencia del factorial, aplicando la documentacion y formato de PEP 8

"""


def factorial(n):
    """
    Calcula el factorial de un número dado de forma recursiva.

    Parametros:
      n ( entero o flotante): El numero del cual se calculara el factorial.

    Retorna:
        entero o flotante: El resultado del calculo factorial.

    Notas de ejecucion:
        n = 4 1era = 24 -> Retorna 4 * factorial(3)
        n = 3 2da = 6   -> Retorna 3 * factorial(2)
        n = 2 3era = 2  -> Retorna 2 * factorial(1)
        n = 1 4ta = 1 -> Retorna 1 (caso base)
    """
    if n == 1: # Caso Base
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
  resultado = factorial(5)
  print(resultado)