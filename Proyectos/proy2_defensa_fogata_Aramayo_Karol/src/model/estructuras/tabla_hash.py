"""
Tabla Hash manual - Almacena puntuaciones de jugadores.

Fase: 12 - Tabla Hash tuplaa registro de jugadores.
"""
import json
import os

ARCHIVO = "puntuaciones.json"


class TablaHash:
    """Tabla hash simple con manejo de colisiones por lista."""

    def __init__(self, tamano=10):
        self.tamano = tamano
        self.contenedor = [[] for _ in range(tamano)]
        

    def _hash(self, clave):
        """Función hash: suma de puntuaciones ASCII de cada carácter."""
        total = 0
        for c in clave:
            total += ord(c)
        return total % self.tamano

    def insertar(self, clave, puntuacion):
        indice = self._hash(clave)
        for tupla in self.contenedor[indice]:
            if tupla[0] == clave:
                if puntuacion > tupla[1]: 
                    tupla[1] = puntuacion
                return
        self.contenedor[indice].append([clave, puntuacion])

    def obtener(self, clave):
        """Devuelve la puntuación de un jugador o None."""
        indice = self._hash(clave)
        for tupla in self.contenedor[indice]:
            if tupla[0] == clave:
                return tupla[1]
        return None

    def existe(self, clave):
        """True si el jugador ya está registrado."""
        return self.obtener(clave) is not None

    def obtener_todas(self):
        """Devuelve todas las puntuaciones como lista de (nombre, puntuacion)."""
        resultado = []
        for bucket in self.contenedor:
            for tupla in bucket:
                resultado.append((tupla[0], tupla[1]))
        resultado.sort(key=lambda x: x[1], reverse=True)
        return resultado

    def guardar(self):
        """Guarda las puntuaciones en un archivo JSON."""
        datos = self.obtener_todas()
        with open(ARCHIVO, "w") as f:
            json.dump(datos, f)

    def cargar(self):
        """Carga las puntuaciones desde un archivo JSON."""
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r") as f:
                datos = json.load(f)
                for nombre, pts in datos:
                    self.insertar(nombre, pts)