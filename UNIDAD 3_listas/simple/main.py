from lista_simple_enlazada import ListaSimpleEnlazada

def ejecutar_pruebas():
    
    lista = ListaSimpleEnlazada()

    print("--- INICIO: Lista Vacía ---")
    lista.recorrido()

    print("\n--- FASE DE INSERCIÓN AL FINAL ---")
    lista.agregar_ultimo(12)
    print("Agregado: 12")
    lista.agregar_ultimo(2)
    print("Agregado: 2")
    lista.agregar_ultimo(25)
    lista.agregar_ultimo(19)
    lista.agregar_ultimo(30)
    lista.recorrido()

    print("\n--- FASE DE ELIMINACIÓN ---")
    lista.eliminar_ultimo()
    print("Eliminado el último (30):")
    lista.recorrido()

    print("\n--- FASE DE INSERCIÓN AL INICIO ---")
    lista.agregar_inicio(10)
    print("Agregado primero (10):")
    lista.recorrido()

    lista.eliminar_inicio()
    print("Eliminado el primero (10):")
    lista.recorrido()

    print("\n--- DATOS DE LOS PUNTEROS Y ESTADO ---")
    print(f"Total de elementos: {lista.get_longitud()}")
    print(f"Puntero 'Primero' apunta al dato: {lista.get_primero()}")
    print(f"Puntero 'Ultimo' apunta al dato:  {lista.get_ultimo()}")


if __name__ == "__main__":
    ejecutar_pruebas()