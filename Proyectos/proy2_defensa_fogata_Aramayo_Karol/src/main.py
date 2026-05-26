"""
Punto de entrada del juego "Defensa de la Fogata".

Fase: 1 - Ventana, game loop y MVC.
"""

import sys
import pygame
from controller.controlador import Controlador


def main() -> None:
    pygame.init()
    controlador = Controlador()
    controlador.iniciar()
    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()