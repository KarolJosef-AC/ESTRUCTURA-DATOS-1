"""
Punto de entrada del juego "Defensa de la Fogata".
====================================================
Fase: 1 - Ventana, game loop y MVC.

Inicializa pygame, crea el controlador y ejecuta el game loop principal.
"""

import sys
import pygame
from controller.controlador import Controlador


def main() -> None:
    """
    Función principal.
    Inicializa pygame, crea el controlador, ejecuta el juego y sale.
    """
    pygame.init()
    controlador = Controlador()
    controlador.iniciar()
    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()