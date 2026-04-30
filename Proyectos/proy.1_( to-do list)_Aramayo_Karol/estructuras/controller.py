from estructuras.model import ListaEnlazada

class Controller:
    """
    Coordina la comunicación entre el Modelo y la Vista.

    Recibe eventos disparados por la Vista, ejecuta la operación
    correspondiente sobre el Modelo y refleja el resultado actualizando
    la interfaz. También gestiona la persistencia en disco.

    Atributos:
        model (ListaEnlazada): Estructura de datos que contiene las tareas.
        vista: Referencia a la capa de presentación.
    """

    def __init__(self, vista):
        self.model = ListaEnlazada()
        self.vista = vista

        # ── Secuencia de Arranque ──
        self.model.cargar_json()    # Restaura la información almacenada en el sistema de archivos
        self._conectar_comandos()   # Enlaza las interacciones visuales con los métodos de control
        self._actualizar_vista()    # Proyecta el estado inicial en la pantalla

    def _conectar_comandos(self):
        """Asigna las acciones del controlador a los comandos de la Vista."""
        self.vista.cmd_agregar   = self.agregar_tarea
        self.vista.cmd_completar = self.completar_tarea
        self.vista.cmd_eliminar  = self.eliminar_tarea

    # ── ACCIONES ─────────────────────────────────────────────

    def agregar_tarea(self):
        """
        Valida y agrega una nueva tarea al modelo.

        Evalúa los campos extraídos del formulario. Ante la ausencia
        de un identificador (título), detiene la ejecución para evitar
        estructuras corruptas.
        """
        # Fase 1: OBTIENE LA INFORMACION DE LA VISTA
        datos = self.vista.obtener_datos_formulario()

        # Fase 2: VALIDACIÓN
        # El título es un requisito estricto
        if not datos["titulo"]:
            self.vista.mostrar_estado("⚠️ El título es obligatorio.")
            return  

        # Fase 3: PROCESAMIENTO. Transferencia de los datos filtrados al Modelo.
        exito, mensaje = self.model.agregar_tarea(
            datos["titulo"],
            datos["descripcion"],
            datos["dificultad"],
        )

        # Fase 4: SINCRONIZACIÓN VISUAL.
        if exito:
            self.model.guardar_json()           # Persistencia en sistema de archivos
            self.vista.limpiar_formulario()     # Restauración de los campos de entrada
            self._actualizar_vista()            # Renderizado de la nueva estructura
            self.vista.mostrar_estado(f"✅ {mensaje}")
        else:
            # Notificación en caso de colisión de datos (nodo ya existente)
            self.vista.mostrar_estado(f"❌ {mensaje}")

    def completar_tarea(self, dato):
        """
        Modifica el atributo de estado de un nodo específico.

        Parametros:
            dato (str): Título de la tarea objetivo.
        """
        # Operación sobre la Lista Enlazada para alterar la propiedad del nodo
        exito, mensaje = self.model.marcar_completada(dato)

        if exito:
            self.model.guardar_json()
            self._actualizar_vista()  
            self.vista.mostrar_estado(f"✅ {mensaje}")
        else:
            self.vista.mostrar_estado(f"❌ {mensaje}")

    def eliminar_tarea(self, dato):
        """
        Exige confirmación explícita previa a la destrucción del nodo.

        Parametros:
            dato (str): Título de la tarea objetivo.
        """
        confirmar = self.vista.mostrar_confirmacion(
            "Confirmar eliminación",
            f"¿Seguro que deseas eliminar '{dato}'?"
        )

        # Respuesta negativa: interrupción del proceso
        if not confirmar:
            return

        # Respuesta positiva: eliminacion del nodo
        exito, mensaje = self.model.eliminar_tarea(dato)

        if exito:
            self.model.guardar_json()
            self._actualizar_vista()
            self.vista.mostrar_estado(f"🗑️ {mensaje}")
        else:
            self.vista.mostrar_estado(f"❌ {mensaje}")

    # ── AUXILIAR ─────────────────────────────────────────────

    def _actualizar_vista(self):
        """Extrae el estado del modelo y ordena su representación."""
        tareas = self.model.obtener_todas()
        self.vista.actualizar_lista(tareas)