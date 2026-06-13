"""
Controlador del juego. Tiene el loop principal.

Fase: 3 - ENEMIGOS
Fase: 4 - Cola y Lista Enlazada.

"""

import pygame
import random # fase 3
from view.render import Render
from model.mapa import Mapa
from model.entidades.fogata import Fogata
from model.entidades.enemigo import Enemigo
from model.estructuras.cola import Cola # Fase 4
from model.estructuras.lista_enlazada import ListaEnlazada # fase 4

ANCHO = 800
ALTO = 600
TITULO = "Defensa de la Fogata"
FPS = 60


class Controlador:
    """Mantiene el juego corriendo. Une la vista y el modelo."""

    def __init__(self) -> None:
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()
        self.render = Render()

        self.mapa = Mapa()
        self.fogata = Fogata(self.mapa)
        
        # FASE 4 - enemigos en estructuras
        self.cola_oleadas = Cola()
        self.activos = ListaEnlazada()
        #
        self.temporizador = 0.0

        # Fase 4 - llenar enemigos en la cola
        for _ in range(10):
            col = random.randint(0, self.mapa.columnas - 1)
            self.cola_oleadas.encolar(Enemigo(col= col, fila = 0))
        # 

        self.run = False
    def eventos(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False

    def _actualizar(self) -> None:
        # Fase 3
        dt = self.clock.get_time() / 1000.0
        self.temporizador += dt

        # Fase 4 - enemigos de la cola a lista enlazada
        if self.temporizador >= 1.5:
            self.temporizador = 0.0
            if not self.cola_oleadas.vacia():
                enemigo = self.cola_oleadas.desencolar()
                self.activos.insertar(enemigo)
        ## fin 

        ## fase 4 - recorrer lista enlazada y no la normal
        for enemigo in self.activos.recorrer():
            llego = enemigo.mover(dt, self.mapa)
            if llego:
                self.fogata.recibir_dano(10)
                self.activos.eliminar(enemigo)
        ## fase 4


    def iniciar(self) -> None:
        self.run = True
        while self.run:
            self.eventos()
            self._actualizar()

            # fase 4 - pasar lista activos al render
            self.render.dibujar(
                self.pantalla,
                self.mapa,
                self.fogata,
                self.activos.recorrer()
            )            
            ## fin

            pygame.display.flip()
            self.clock.tick(FPS)