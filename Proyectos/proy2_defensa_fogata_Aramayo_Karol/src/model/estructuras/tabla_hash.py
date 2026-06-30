"""
Tabla Hash manual - Almacena puntuaciones de jugadores.
=========================================================
Fase: 12 - Tabla Hash para registro de jugadores.

Función hash: suma de valores ASCII del nombre módulo tamaño.
Manejo de colisiones: encadenamiento (lista por bucket).
Persistencia: archivo JSON.
"""

import json
import os

ARCHIVO = "puntuaciones.json"


class TablaHash:
    """
    Tabla hash simple con manejo de colisiones por lista encadenada.
    
    Usada para buscar puntuaciones por nombre de jugador en O(1) promedio.
    """

    def __init__(self, tamano: int = 10):
        """
        Inicializa la tabla hash con buckets vacíos.
        
        Args:
            tamano: Número de buckets (default 10).
        """
        self.tamano = tamano
        self.contenedor = [[] for _ in range(tamano)]

    def _hash(self, clave: str) -> int:
        """
        Función hash: suma de valores ASCII de cada carácter.
        
        Args:
            clave: Nombre del jugador.
            
        Returns:
            int: Índice del bucket (0 a tamano-1).
        """
        total = 0
        for c in clave:
            total += ord(c)
        return total % self.tamano

    def insertar(self, clave: str, puntuacion: int) -> None:
        """
        Inserta o actualiza la puntuación de un jugador.
        Solo actualiza si la nueva puntuación es mayor.
        
        Args:
            clave: Nombre del jugador.
            puntuacion: Puntuación obtenida.
        """
        indice = self._hash(clave)
        for tupla in self.contenedor[indice]:
            if tupla[0] == clave:
                if puntuacion > tupla[1]:
                    tupla[1] = puntuacion
                return
        self.contenedor[indice].append([clave, puntuacion])

    def obtener(self, clave: str) -> int:
        """
        Obtiene la puntuación de un jugador.
        
        Args:
            clave: Nombre del jugador.
            
        Returns:
            int o None: Puntuación del jugador o None si no existe.
        """
        indice = self._hash(clave)
        for tupla in self.contenedor[indice]:
            if tupla[0] == clave:
                return tupla[1]
        return None

    def existe(self, clave: str) -> bool:
        """
        Verifica si un jugador ya está registrado.
        
        Args:
            clave: Nombre del jugador.
            
        Returns:
            bool: True si existe.
        """
        return self.obtener(clave) is not None

    def obtener_todas(self) -> list:
        """
        Devuelve todas las puntuaciones ordenadas de mayor a menor.
        
        Returns:
            list: Lista de tuplas (nombre, puntuacion).
        """
        resultado = []
        for bucket in self.contenedor:
            for tupla in bucket:
                resultado.append((tupla[0], tupla[1]))
        resultado.sort(key=lambda x: x[1], reverse=True)
        return resultado

    def guardar(self) -> None:
        """
        Persiste las puntuaciones en un archivo JSON.
        """
        datos = self.obtener_todas()
        with open(ARCHIVO, "w") as f:
            json.dump(datos, f)

    def cargar(self) -> None:
        """
        Carga las puntuaciones desde el archivo JSON.
        Si el archivo no existe, no hace nada.
        """
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r") as f:
                datos = json.load(f)
                for nombre, pts in datos:
                    self.insertar(nombre, pts)