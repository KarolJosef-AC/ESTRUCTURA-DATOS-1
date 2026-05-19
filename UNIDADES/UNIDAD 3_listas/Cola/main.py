from cola import Cola

def main():
    cola = Cola()
    
    print("=== COLA (FIFO) ===\n")
    
    cola.encolar(10)
    cola.encolar(20)
    cola.encolar(30)
    cola.mostrar()
    
    print(f"\nFrente: {cola.ver_frente()}")
    print(f"Tamanio: {cola.obtener_tamanio()}\n")
    
    cola.desencolar()
    cola.mostrar()
    
    cola.desencolar()
    cola.desencolar()
    cola.desencolar()
    
    print(f"\n¿Vacia? {cola.esta_vacia()}")

if __name__ == "__main__":
    main()