"""
Lógica de acciones del juego.
===============================
Contiene los métodos que el planificador ejecuta.
Separado del controlador para mantener MVC limpio.

El controlador ORQUESTA.
El planificador ORDENA.
Este archivo EJECUTA las acciones.
"""

import random
from model.entidades.proyectil import Proyectil
from model.entidades.enemigo import Enemigo
from model.mapa import TAM_CELDA


class LogicaJuego:
    """
    Contiene la lógica de cada acción del juego.
    
    Cada método corresponde a una prioridad del planificador:
        verificar_llegada  -> Prioridad 0 (CRÍTICO)
        disparar_torre     -> Prioridad 1 (ALTO)
        spawnear_enemigo   -> Prioridad 2 (NORMAL)
        mover_proyectiles  -> Prioridad 2 (NORMAL)
        verificar_nueva_oleada -> Prioridad 2 (NORMAL)
        limpiar_y_atacar   -> Prioridad 3 (BAJO)
    """

    def __init__(self, controlador):
        """
        Guarda referencia al controlador para acceder a los datos del juego.
        
        Args:
            controlador: Instancia del Controlador principal.
        """
        self.c = controlador

    def verificar_llegada(self, enemigo, dt):
        """
        Verifica si un enemigo llegó a la fogata.
        Si llegó: aplica daño, elimina enemigo, verifica fin del juego.
        Mide el tiempo de ejecución del proceso.
        
        Args:
            enemigo: Enemigo a verificar.
            dt: Delta time del frame.
        """
        llego = enemigo.mover(dt, self.c.mapa)
        if llego:
            t = self.c.tiempo_juego - enemigo.tiempo_salida
            print(f"  [PROCESO] {enemigo.tipo} | {t:.1f}s | LLEGO A FOGATA")
            self.c.fogata.recibir_dano(10)
            self.c.activos.eliminar(enemigo)
            if not self.c.fogata.esta_viva():
                self.c.estado = "fin_derrota"
                if self.c.jugador:
                    self.c.tabla_hash.insertar(self.c.jugador, self.c.puntuacion)
                    self.c.tabla_hash.guardar()

    def disparar_torre(self, defensa):
        """
        Una torre busca al enemigo más cercano en su rango y le dispara.
        
        Args:
            defensa: Defensa de tipo 'torre' que va a disparar.
        """
        if not defensa.puede_disparar(self.c.tiempo_juego):
            return

        RANGO_TORRE = 5 * TAM_CELDA
        mejor = None
        mejor_dist = RANGO_TORRE
        for e in self.c.activos.recorrer():
            dx = e.x - defensa.col * TAM_CELDA
            dy = e.y - defensa.fila * TAM_CELDA
            dist = (dx**2 + dy**2) ** 0.5
            if dist < mejor_dist:
                mejor_dist = dist
                mejor = e

        if mejor:
            self.c.proyectiles.append(
                Proyectil(defensa.col, defensa.fila, mejor)
            )

    def spawnear_enemigo(self):
        """
        Saca un enemigo de la cola FIFO y lo pone en el campo.
        Si la celda de inicio está ocupada, lo devuelve al final de la cola.
        Registra el tiempo de salida para medir su ejecución.
        """
        if not self.c.cola_oleadas.vacia():
            enemigo = self.c.cola_oleadas.desencolar()

            if self.c.mapa.libre(enemigo.col, enemigo.fila):
                enemigo.tiempo_salida = self.c.tiempo_juego
                self.c.activos.insertar(enemigo)
            else:
                # Celda ocupada: volver al final de la cola
                self.c.cola_oleadas.encolar(enemigo)

    def mover_proyectiles(self, dt):
        """
        Mueve todos los proyectiles hacia sus objetivos.
        Elimina los que ya no están activos.
        
        Args:
            dt: Delta time del frame.
        """
        for p in self.c.proyectiles[:]:
            p.mover(dt)
            if not p.activo or p.fuera_de_pantalla():
                self.c.proyectiles.remove(p)

    def verificar_nueva_oleada(self):
        """
        Si no hay enemigos en cola ni activos, genera una nueva oleada.
        El tipo de enemigo lo decide según la oleada.
        """
        if self.c.cola_oleadas.vacia() and self.c.activos.vacia():
            self.c.oleada += 1
            cantidad = 10 + self.c.oleada * 2
            for _ in range(cantidad):
                col = random.randint(0, self.c.mapa.columnas - 1)
                tipo = self.decidir_tipo_enemigo(self.c.oleada)
                self.c.cola_oleadas.encolar(Enemigo(col=col, fila=0, tipo=tipo))

    def limpiar_y_atacar(self, dt):
        """
        Elimina enemigos muertos (otorga puntuación y oro).
        Procesa ataques de enemigos a defensas.
        Mide tiempo de ejecución de cada enemigo eliminado.
        
        Args:
            dt: Delta time del frame.
        """
        # Fase 1: Recolectar enemigos muertos
        muertos = []
        for enemigo in self.c.activos.recorrer():
            if not enemigo.esta_vivo():
                muertos.append(enemigo)

        # Fase 2: Eliminar los muertos
        for enemigo in muertos:
            t = self.c.tiempo_juego - enemigo.tiempo_salida
            print(f"  [PROCESO] {enemigo.tipo} | {t:.1f}s | MUERTO")
            self.c.activos.eliminar(enemigo)
            self.c.puntuacion += 10
            self.c.oro += 10

        # Fase 3: Enemigos vivos atacan defensas
        for enemigo in self.c.activos.recorrer():
            fila_abajo = enemigo.fila + 1
            if fila_abajo >= self.c.mapa.filas:
                continue
            if self.c.mapa.libre(enemigo.col, fila_abajo):
                continue
            for d in self.c.defensas:
                if d.col == enemigo.col and d.fila == fila_abajo:
                    dano = 15 if enemigo.tipo == "tanque" else 5
                    d.recibir_dano(dano * dt)
                    if d.destruida():
                        self.c.mapa.poner(d.col, d.fila, 0)
                        self.c.defensas.remove(d)
                    break

    def decidir_tipo_enemigo(self, oleada: int) -> str:
        """
        Decide el tipo de enemigo según la oleada.
        Cada 3 oleadas hay probabilidad de enemigos rápidos.

        Args: 
            oleada: Número de oleada actual
            
        Returns:
            str: Tipo de enemigo ('normal', 'tanque', 'rapido')
        """
        if oleada % 3 == 0 and random.random() < 0.3:
            return "rapido"
        return random.choice(["normal", "normal", "tanque"])