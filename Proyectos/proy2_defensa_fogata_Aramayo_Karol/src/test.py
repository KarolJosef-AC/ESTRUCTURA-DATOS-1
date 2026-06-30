import pygame
import random
import sys
import json
import os

from model.mapa import Mapa, COLUMNAS, FILAS, TAM_CELDA, CELDA_LIBRE, CELDA_OBSTACULO, CELDA_FOGATA
from model.entidades.fogata import Fogata
from model.entidades.enemigo import Enemigo
from model.entidades.defensa import Defensa
from model.entidades.proyectil import Proyectil
from model.estructuras.cola import Cola
from model.estructuras.lista_enlazada import ListaEnlazada, Nodo
from model.estructuras.tabla_hash import TablaHash
from view.render import Render
from controller.controlador import Controlador



# TRAZA 1: Ver la grilla al inicio
print("=" * 50)
print("TRAZA 1: Grilla inicial del mapa")
print("=" * 50)

mapa = Mapa()
fogata = Fogata(mapa)

print("\nGrilla 20x15 (0=libre, 1=obstáculo, 2=fogata):")
for fila in mapa.grilla:
    print(fila)

print("=" * 50)
print("TRAZA 2: defensa")
print("=" * 50)

defensa = Defensa(col=5, fila=10, tipo="valla")
defensa.colocar_en_mapa(mapa)


print(mapa.grilla[10])