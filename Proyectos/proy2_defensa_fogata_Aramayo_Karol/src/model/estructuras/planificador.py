"""
Planificador de Acciones del Juego.
=====================================
Fase: B - Planificador de Procesos.

Problema que resuelve:
    En cada frame ocurren múltiples acciones concurrentes.
    Sin un planificador, se ejecutan en orden arbitrario.
    El planificador asigna PRIORIDAD a cada acción y las ejecuta
    en orden de urgencia: crítico primero, limpieza al final.

Prioridades:
    0 = CRÍTICO: Daño a fogata (puede terminar el juego)
    1 = ALTO:    Disparos de torres (elimina amenazas)
    2 = NORMAL:  Spawn, movimiento de proyectiles, oleada
    3 = BAJO:    Limpieza de muertos y ataques a defensas
"""


class AccionJuego:
    """
    Representa UNA acción que el juego debe ejecutar en el frame.

    Atributos:
        prioridad (int): Urgencia (0 = más urgente).
        descripcion (str): Etiqueta para el panel del planificador.
        ejecutar (callable): Función sin parámetros a invocar.
    """

    def __init__(self, prioridad: int, descripcion: str, ejecutar):
        """
        Inicializa una acción del juego.

        Args:
            prioridad: Número de urgencia (0 = crítico).
            descripcion: Texto visible en el panel del planificador.
            ejecutar: Función a invocar al ejecutar esta acción.
        """
        self.prioridad   = prioridad
        self.descripcion = descripcion
        self.ejecutar    = ejecutar

    def __lt__(self, otra: "AccionJuego") -> bool:
        """Orden por prioridad: menor número = más urgente."""
        return self.prioridad < otra.prioridad

    def __repr__(self) -> str:
        return f"Accion(p={self.prioridad}, '{self.descripcion}')"


class PlanificadorAcciones:
    """
    Planificador de procesos del juego.

    Inserta acciones ordenadas por prioridad y las ejecuta en ese orden.
    Al finalizar el frame, la lista queda vacía para el siguiente.

    Constantes de prioridad:
        CRITICO = 0
        ALTO    = 1
        NORMAL  = 2
        BAJO    = 3
    """

    CRITICO = 0
    ALTO    = 1
    NORMAL  = 2
    BAJO    = 3

    def __init__(self) -> None:
        """Inicializa el planificador sin acciones pendientes."""
        self._acciones = []
        self._contador = 0

    def registrar(self, prioridad: int, descripcion: str, funcion) -> None:
        """
        Agrega una acción manteniendo el orden por prioridad.

        La lista permanece ordenada después de cada inserción:
        menor número de prioridad → posición más al frente.

        Args:
            prioridad: Urgencia (usar constantes de clase).
            descripcion: Texto visible en el panel del planificador.
            funcion: Función sin parámetros a ejecutar.
        """
        accion = AccionJuego(prioridad, descripcion, funcion)

        insertado = False
        for i, existente in enumerate(self._acciones):
            if accion < existente:
                self._acciones.insert(i, accion)
                insertado = True
                break

        if not insertado:
            self._acciones.append(accion)

    def ejecutar_frame(self) -> None:
        """
        Ejecuta todas las acciones del frame en orden de prioridad.

        Imprime en consola cada 60 frames (1 vez por segundo a 60 FPS).
        Al terminar, la lista queda vacía para el siguiente frame.
        """
        self._contador += 1

        if self._contador % 60 == 0:
            print(f"\n[PLANIFICADOR] Frame {self._contador}: "
                  f"{len(self._acciones)} acciones")
            for accion in self._acciones:
                print(f"  -> [{accion.prioridad}] {accion.descripcion}")

        while self._acciones:
            accion = self._acciones.pop(0)
            accion.ejecutar()

    def limpiar(self) -> None:
        """Vacía todas las acciones pendientes (fin de partida)."""
        self._acciones.clear()

    def pendientes(self) -> int:
        """
        Cantidad de acciones en espera para este frame.

        Returns:
            int: Número de acciones pendientes.
        """
        return len(self._acciones)