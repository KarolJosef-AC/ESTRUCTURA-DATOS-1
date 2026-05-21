import json
import os

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.estado = "pendiente"
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
        self.CAPACIDAD_MAXIMA = 100

        # ── CÁLCULO DE RUTA ABSOLUTA ──
        # 1. Directorio actual: .../estructuras
        directorio_estructuras = os.path.dirname(os.path.abspath(__file__))
        # 2. Directorio raíz: .../proy.1_( to-do list)_Aramayo_Karol
        directorio_raiz = os.path.dirname(directorio_estructuras)
        # 3. Ruta final del archivo
        self.RUTA_ARCHIVO = os.path.join(directorio_raiz, "datos", "tareas.json")

    def agregar_tarea(self, dato):
        if self.tamanio >= self.CAPACIDAD_MAXIMA:
            return False, "Lista llena. Capacidad maxima alcanzada"
        if self._existe_tarea(dato):
            return False, f"La tarea '{dato}' ya existe."
        
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamanio += 1
        return True, f"Tarea '{dato}' agregada correctamente."

    def _existe_tarea(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.lower() == dato.lower():
                return True
            actual = actual.siguiente
        return False

    def marcar_completada(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.lower() == dato.lower():
                if actual.estado == "completada":
                    return False, f"'{dato}' ya estaba completada."
                actual.estado = "completada"
                return True, f"tarea '{dato}' marcada como completada."
            actual = actual.siguiente
        return False, f"No se encontro la tarea '{dato}'."

    def eliminar_tarea(self, dato):
        if self.cabeza is None:
            return False, "La lista esta vacia."
        
        if self.cabeza.dato.lower() == dato.lower():
            self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
            return True, f"Tarea '{dato}' eliminada."

        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.dato.lower() == dato.lower():
                anterior.siguiente = actual.siguiente
                self.tamanio -= 1
                return True,f"Tarea '{dato}' eliminada."
            anterior = actual
            actual = actual.siguiente
        return False, f"No se encontro la tarea '{dato}'."

    def obtener_todas(self):
        tareas = []
        actual = self.cabeza
        while actual is not None:
            tareas.append({
                "dato" : actual.dato,
                "estado": actual.estado
            })
            actual = actual.siguiente
        return tareas

    # ── PERSISTENCIA SEGURA ──

    def guardar_json(self):
        # Aseguramos que la carpeta "datos" se cree en la raíz
        directorio_datos = os.path.dirname(self.RUTA_ARCHIVO)
        os.makedirs(directorio_datos, exist_ok=True)
        
        datos = self.obtener_todas()
        with open(self.RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)

    def cargar_json(self):
        # 1. Si no existe, salimos
        if not os.path.exists(self.RUTA_ARCHIVO):
            return
        
        # 2. Si existe pero está vacío (peso 0), salimos para evitar el JSONDecodeError
        if os.path.getsize(self.RUTA_ARCHIVO) == 0:
            return

        try:
            with open(self.RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            for tarea in datos:
                exito, _ = self.agregar_tarea(tarea["dato"])
                if exito and tarea.get("estado") == "completada":
                    self.marcar_completada(tarea["dato"])
        except Exception:
            pass 