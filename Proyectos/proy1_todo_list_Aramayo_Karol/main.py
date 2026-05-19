import customtkinter as ctk
from estructuras.view import Vista
from estructuras.controller import Controller

def main():
    """Punto de inicialización del patrón Modelo-Vista-Controlador."""
    # 1. Creación de la instancia base del gestor de ventanas
    root = ctk.CTk()
    
    # 2. Inicialización de la capa visual pasando el objeto raíz
    vista = Vista(root)
    
    # 3. Construye el Modelo de forma interna
    Controller(vista)
    
    # 4. Espera de eventos del sistema o del usuario
    root.mainloop()

if __name__ == "__main__":
    main()