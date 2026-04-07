"""
Listas de Comprensión y Filtrado

Transforma y filtra una secuencia de datos numéricos en una sola operación, reduciendo el tiempo de evaluación

"""

def buscar_patron_texto(texto_completo, palabra_objetivo):
    """
    Determina la existencia de una secuencia específica de caracteres dentro de una muestra mayor.

    Parametros:
        texto_completo (cadena): El bloque de información textual que será analizado.
        palabra_objetivo (cadena): La secuencia exacta de caracteres que se desea localizar.

    Retorna:
        booleano: True si la secuencia existe en la muestra, False en caso contrario.
    """

    texto_normalizado = texto_completo.lower()
    objetivo_normalizado = palabra_objetivo.lower()

    if objetivo_normalizado in texto_normalizado:
        return True
    else:
        return False

if __name__ == "__main__":
      texto = "Que buen clima hace el dia de hoy"
      palabra_buscada = "clima"
      resultado_busqueda = buscar_patron_texto(texto, palabra_buscada)
      print(resultado_busqueda)
