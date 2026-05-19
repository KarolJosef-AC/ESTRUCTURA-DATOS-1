from pila import Pila

def main():
    cola = Pila()
    
    print("=== PILA === \n")
    
    cola.apilar(10)
    cola.apilar(20)
    cola.apilar(30)
    cola.mostrar()
    
    print(f"\nCima: {cola.ver_cima()}")
    print(f"Tamaño: {cola.tamaño()}\n")
    
    cola.desapilar()
    cola.mostrar()
    
    cola.desapilar()
    cola.desapilar()
    cola.desapilar()  
    
    print(f"\n¿Está vacía? {cola.esta_vacia()}")

if __name__ == "__main__":
    main()