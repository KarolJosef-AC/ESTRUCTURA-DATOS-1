import json
import os

class Nodo:
    """
    Unidad de almacenamiento de la lista enlazada.

    Representa una tarea individual con todos sus atributos.
    El campo `siguiente` mantiene el enlace al próximo nodo de la cadena.

    Parametros:
        dato (str): Título identificador de la tarea.
        descripcion (str): Detalle adicional opcional.
        dificultad (str): Nivel de esfuerzo ("Facil", "Media", "Dificil").
    """
    def __init__(self, dato, descripcion="", dificultad="Media"):
        self.dato = dato
        self.descripcion = descripcion
        self.dificultad = dificultad
        self.estado = "pendiente"
        self.siguiente = None

class ListaEnlazada:
    """
    Lista enlazada simple para la gestión de tareas.

    Almacena nodos en orden de inserción (FIFO). Provee operaciones de
    agregar, completar y eliminar tareas, junto con persistencia
    automática en JSON.

    Atributos:
        cabeza (Nodo | None): Primer nodo de la cadena.
        tamanio (int): Cantidad de tareas almacenadas.
        CAPACIDAD_MAXIMA (int): Límite fijo de nodos permitidos.
        RUTA_ARCHIVO (str): Ruta absoluta al archivo de persistencia.
    """
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
        self.CAPACIDAD_MAXIMA = 100

        ruta_archivo = os.path.abspath(__file__) # dir. del archivo(model)
        directorio_estructura = os.path.dirname(ruta_archivo) # dir. de la carpeta donde esta el model (estructuras)
        self.raiz_proyecto = os.path.dirname(directorio_estructura) # dir. de la carpeta del proyecto
        self.RUTA_ARCHIVO = os.path.join( #.join = creacion de una ruta en la raiz principal ( solo ruta nada mas)
                self.raiz_proyecto, "datos", "tareas.json"
        )

    # OPERACIONES
    def agregar_tarea(self, dato, descripcion = "", dificultad = "Media", estado = "pendiente"):
        """
        Inserta una nueva tarea al final de la lista.

        Rechaza la inserción si la lista alcanzó su capacidad máxima o
        si ya existe una tarea con el mismo título (sin distinción de
        mayúsculas). En caso de éxito, encadena el nuevo nodo al final
        y actualiza el contador.

        Parametros:
            dato (str): Título de la tarea. Actúa como identificador único.
            descripcion (str): Información adicional opcional.
            dificultad (str): "Facil", "Media" o "Dificil".
            estado (str): Estado inicial de la tarea, por defecto "pendiente".

        Retorna:
            tuple[bool, str]: (True, mensaje de éxito) si la tarea fue
                insertada, o (False, motivo) si fue rechazada.
        """
        # CASO 1: Supero la capacidad maxima
        if self.tamanio >= self.CAPACIDAD_MAXIMA:
            return False, "Lista llena. Capacidad Maxima alcanzada"
        # CASO 2: Ya existe
        if self._existe_tarea(dato):
            return False, f"La tarea '{dato}' ya existe"
        
        nuevo_nodo = Nodo(dato, descripcion, dificultad)
        nuevo_nodo.estado = estado
        # CASO 3: Lista vacia
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
        # CASO 4: Hay mas elementos -> Recorrer lista
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamanio += 1
        return True, f"Tarea '{dato}' agregada correctamente."
    
    def marcar_completada(self, dato):
        """
        Cambia el estado de una tarea a "completada".

        Recorre la lista secuencialmente buscando el nodo cuyo título
        coincida con `dato`. No modifica tareas que ya estén completadas.

        Parametros:
            dato (str): Título de la tarea a completar.

        Retorna:
            tuple[bool, str]: (True, confirmación) si el estado fue
                actualizado, o (False, motivo) si no se encontró la
                tarea o ya estaba completada.
        """
        actual = self.cabeza
        while actual is not None:
            #CASO 1: nodo encontrado
            if actual.dato.lower() == dato.lower():
                #Sub-caso 1: ya estaba completada
                if actual.estado == "completada":
                    return False, f"La tarea '{dato}' ya estaba completada." 
                # Si no estaba la marcamos completada
                actual.estado = "completada"
                return True, f"La tarea '{dato}' marcada como completada."
            actual = actual.siguiente
        # CASO 2: no se encontro la tarea
        return False, f"No se encontró la tarea '{dato}'."
    
    def eliminar_tarea(self, dato):
        """
        Desvincula y descarta el nodo que corresponde a `dato`.

        Maneja el caso especial donde el nodo a eliminar es la cabeza.
        Para los demás nodos, mantiene el puntero `anterior` para
        reconectar la cadena saltando el nodo eliminado.

        Parametros:
            dato (str): Título de la tarea a eliminar.

        Retorna:
            tuple[bool, str]: (True, confirmación) si la tarea fue
                eliminada, o (False, motivo) si la lista estaba vacía
                o no se encontró la tarea.
        """
        # Caso 1: Lista vacia
        if self.cabeza is None:
            return False, "Lista Vacia."
        
        # Caso 2: Nodo a eliminar es la cabeza
        if self.cabeza.dato.lower() == dato.lower():
            self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
            return True, f"La tarea '{dato}' eliminada."

        # Caso 3: Nodo en medio o final 
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:       
            if actual.dato.lower() == dato.lower():
                anterior.siguiente = actual.siguiente # saltamos el nodo actual, a si siguiente
                self.tamanio -= 1
                return True, f"La tarea '{dato}' eliminada."
            # AVANZAMOS: anterior donde actual y actual al siguiente
            anterior = actual
            actual = actual.siguiente
        
        # CASO 4: No se encontro el nodo
        return False, f"No se encontró la tarea '{dato}'."
    
    def obtener_todas(self):
        """
        Retorna todas las tareas como lista de diccionarios.

        Recorre la lista completa nodo por nodo y convierte cada tarea
        en un diccionario legible para la estructura de la Vista.

        Retorna:
            list[dict]: Lista con los atributos de cada tarea.
        """
        tareas = []
        actual = self.cabeza
        while actual is not None:
            tareas.append({
                "dato" :        actual.dato,
                "descripcion":  actual.descripcion,
                "dificultad":   actual.dificultad,
                "estado":       actual.estado,
            })
            actual = actual.siguiente
        return tareas

    # AUXILIARES
    def _existe_tarea(self, dato):
        """
        Verifica si ya existe un nodo con el mismo título.

        Parametros:
            dato (str): Título a buscar (sin distinción de mayúsculas).

        Retorna:
            bool: True si existe un nodo coincidente, False en caso contrario.
        """
        actual = self.cabeza
        while actual is not None:
            if actual.dato.lower() == dato.lower():
                return True
            actual = actual.siguiente
        return False
    
    # PERSISTENCIA
    def guardar_json(self):
        """
        Serializa toda la lista al archivo JSON.

        Crea la carpeta `datos/` si no existe antes de escribir.
        Sobrescribe el archivo completo en cada llamada.
        """
        # CREACION DE CARPETA: DATOS
        carpeta_datos = os.path.dirname(self.RUTA_ARCHIVO)
        os.makedirs(carpeta_datos, exist_ok=True) # crea carpeta si no existe
        with open(self.RUTA_ARCHIVO, "w", encoding="utf-8") as f: #with: cierra archivo aunque colapse el programa
            json.dump(self.obtener_todas(), f, ensure_ascii=False, indent=2) # ident: saltos para lectura

    def cargar_json(self):
        """
        Lee el archivo JSON y reconstruye la lista enlazada al iniciar.

        Reutiliza `agregar_tarea` para reconstruir el estado exacto
        guardado, incluyendo el estado de cada tarea. Si el archivo no
        existe, está vacío o tiene formato inválido, termina de forma
        controlada.
        """
        # CASO 1: el archivo no existe o esta vacio
        if not os.path.exists(self.RUTA_ARCHIVO) or \
                os.path.getsize(self.RUTA_ARCHIVO) == 0:
            return
        try:
            with open(self.RUTA_ARCHIVO, "r", encoding="utf-8") as f:
                datos = json.load(f)

            # Reconstruye el nodo reusando agregar_tarea
            for t in datos:
                self.agregar_tarea(
                    dato = t["dato"], 
                    descripcion = t.get("descripcion", ""),
                    dificultad = t.get("dificultad", "Media"),
                    estado = t.get("estado", "pendiente")
                )
        
        except json.JSONDecodeError:
            # CASO 2: Archivo corrupto
            pass