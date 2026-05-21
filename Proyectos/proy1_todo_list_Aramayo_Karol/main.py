import tkinter as tk
from estructuras.model import ListaEnlazada
from estructuras.view import Vista
from estructuras.controller import Controller

def main():
    root = tk.Tk()
    
    # 1. Crear el Modelo
    modelo = ListaEnlazada()
    
    # 2. Crear la Vista
    vista = Vista(root)
    
    # 3. Crear el Controlador uniendo el Modelo y la Vista
    controlador = Controller(modelo, vista)
    
    # 4. Iniciar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()