class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.cmd_agregar = self.agregar
        self.view.cmd_completar = self.completar
        self.view.cmd_eliminar = self.eliminar

        self.model.cargar_json()
        self.actualizar_pantalla()

    def agregar(self):
        tarea = self.view.obtener_texto_entrada()
        if not tarea:
            return

        exito, mensaje = self.model.agregar_tarea(tarea)
        if exito:
            self.model.guardar_json()
            self.view.limpiar_entrada()
            self.actualizar_pantalla()
            self.view.mostrar_estado(mensaje)
        else:
            self.view.mostrar_mensaje("Error", mensaje, "error")

    def completar(self):
        tarea = self.view.obtener_seleccion()
        if not tarea:
            self.view.mostrar_mensaje("Aviso", "Seleccione una tarea primero.", "advertencia")
            return

        exito, mensaje = self.model.marcar_completada(tarea)
        if exito:
            self.model.guardar_json()
            self.actualizar_pantalla()
            self.view.mostrar_estado(mensaje)
        else:
            self.view.mostrar_mensaje("Error", mensaje, "error")

    def eliminar(self):
        tarea = self.view.obtener_seleccion()
        if not tarea:
            self.view.mostrar_mensaje("Aviso", "Seleccione una tarea primero.", "advertencia")
            return

        exito, mensaje = self.model.eliminar_tarea(tarea)
        if exito:
            self.model.guardar_json()
            self.actualizar_pantalla()
            self.view.mostrar_estado(mensaje)
        else:
            self.view.mostrar_mensaje("Error", mensaje, "error")

    def actualizar_pantalla(self):
        tareas = self.model.obtener_todas()
        self.view.actualizar_lista(tareas)