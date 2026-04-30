import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# CONFIGURACION GLOBAL --------------------------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

COLORES = {
    "fondo":         "#1A1A1A",  # fondo general oscuro, no negro puro
    "header":        "#2D6A4F",  # verde oscuro para la barra superior
    "tarjeta":       "#2A2A2A",  # gris oscuro para las tarjetas
    "texto_titulo":  "#E8F5E9",  # blanco verdoso para títulos
    "texto_desc":    "#81C784",  # verde claro para descripciones
    "negro":         "#000000",  # negro puro (formulario inferior)
    "gris":          "#A89DC0",  # mantenido por compatibilidad
    "oscuro":        "#3D3460",  # mantenido por compatibilidad
}

COLOR_DIFICULTAD = {
    "Facil":   "#86EFAC",
    "Media":   "#FDE68A",
    "Dificil": "#FCA5A5",
}

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        self._construir_pantalla()

    def _construir_pantalla(self):
        self._barra_superior()
        self._zona_tareas()
        self._formulario()

    # ZONA DE BARRA SUPERIOR ----------------------------------------------------------
    def _barra_superior(self):
        """Cabecera con identificación y módulo de notificación de estado."""
        barra = ctk.CTkFrame(self.root, 
                             fg_color=COLORES["header"],
                             corner_radius=0, 
                             height=55)
        barra.pack(fill="x")
        barra.pack_propagate(False)

        self._crear_titulo_app(barra)
        self._crear_etiqueta_estado(barra)

    def _crear_titulo_app(self, contenedor_padre):
        """Genera y posiciona el título principal en el lado izquierdo."""
        self.titulo = ctk.CTkLabel(contenedor_padre, 
                                   text="📝 Mis Tareas",
                                   font=ctk.CTkFont(size=22, weight="bold"),
                                   text_color=COLORES["texto_titulo"])
        self.titulo.pack(side="left", padx=20)
    
    def _crear_etiqueta_estado(self, contenedor_padre):
        """Genera y posiciona el texto dinámico en el lado derecho."""
        self.lbl_estado = ctk.CTkLabel(contenedor_padre,
                                       text="Listo.",
                                       font=ctk.CTkFont(size=15),
                                       text_color=COLORES["texto_titulo"])
        self.lbl_estado.pack(side="right", padx=20)


    # ZONA DE TAREAS  ----------------------------------------------------------
    
    def _zona_tareas(self): 
        """Contenedor general de todas las tareas"""
        self.contenedor = ctk.CTkScrollableFrame(self.root,
                                                 fg_color=COLORES["fondo"],
                                                 scrollbar_button_color=COLORES["header"],
                                                 corner_radius=0)
        self.contenedor.pack(fill="both",
                             expand=True,
                             padx=10,
                             pady=8)
        
    def _formulario(self):
        """Crea la base y delega la construcción interna."""
        form = ctk.CTkFrame(self.root,
                            fg_color=COLORES["negro"],
                            corner_radius=10)
        form.pack(fill="x", padx=10, pady=(0, 10))
        self._crear_inputs_principales(form)
        self._crear_controles_accion(form)
        self._configurar_grid_formulario(form)

    def _crear_inputs_principales(self, contenedor):
        """Fila 0: Captura de Título y Descripción."""
        self.campo_titulo = ctk.CTkEntry(contenedor,
                                         placeholder_text="Titulo *",
                                         height=34)
        self.campo_titulo.grid(row=0,
                               column=0,
                               padx=(12, 4),
                               pady=8,
                               sticky="ew")
        
        self.campo_descripcion = ctk.CTkEntry(contenedor,
                                              placeholder_text="Descripcion",
                                              height=34)
        self.campo_descripcion.grid(row=0,
                                    column=1,
                                    padx=(4, 12),
                                    pady=8,
                                    sticky="ew")

    def _crear_controles_accion(self, contenedor):
        """Fila 1: Selector de categoría y botón de agregar."""
        self.selector_dif = ctk.CTkOptionMenu(contenedor,
                                              values=["Facil", "Media", "Dificil"],
                                              height=34)
        self.selector_dif.set("Media")
        self.selector_dif.grid(row=1, 
                               column=0,
                               padx=(12, 4),
                               pady=(0, 8),
                               sticky="ew")
        
        boton_agregar = ctk.CTkButton(contenedor,
                                      text="➕ Agregar",
                                      height=34,
                                      command=lambda: self.cmd_agregar())
        boton_agregar.grid(row=1,
                           column=1,
                           padx=(4, 12),
                           pady=(0, 8),
                           sticky="ew")

    def _configurar_grid_formulario(self, contenedor):
        """Ajuste de expansión de las columnas."""
        contenedor.grid_columnconfigure(0, weight=1)
        contenedor.grid_columnconfigure(1, weight=1)

    # TARJETAS ------------------------------------------------
    def actualizar_lista(self, tareas):
        """Actualizador del contenedor de tareas."""
        self._limpiar_contenedor()
        if not tareas:
            self._dibujar_estado_vacio()
        else:
            for tarea in tareas:
                self._tarjeta(tarea)

    def _limpiar_contenedor(self):
        """Elimina todos los widgets del contenedor de scroll."""
        for widget in self.contenedor.winfo_children():
            widget.destroy()

    def _dibujar_estado_vacio(self):
        """Mensaje cuando la lista de la estructura está vacía."""
        ctk.CTkLabel(
            self.contenedor,
            text="¡No hay tareas! 🎉",
            font=ctk.CTkFont(size=18),
            text_color=COLORES["texto_desc"]
        ).pack(pady=30)

    def _tarjeta(self, tarea):
        """Crea la estructura base de la tarjeta y delega sus componentes internos."""
        completada = tarea["estado"] == "completada"
        color_dif = COLOR_DIFICULTAD.get(tarea["dificultad"], "#ccc")
        
        card = ctk.CTkFrame(self.contenedor,
                            fg_color=COLORES["tarjeta"],
                            border_color=COLORES["header"],
                            border_width=1,
                            corner_radius=8)
        card.pack(fill="x", pady=2)
        card.grid_columnconfigure(1, weight=1)

        self._crear_indicador_dificultad(card, color_dif)
        self._crear_cuerpo_texto(card, tarea, completada)
        self._crear_acciones_tarjeta(card, tarea["dato"], completada)

    def _crear_indicador_dificultad(self, card, color):
        """Sub-componente: Línea vertical de color (Izquierda)."""
        tk.Frame(card, 
                 bg=color, 
                 width=6).grid(row=0, column=0, sticky="ns")
        
    def _crear_cuerpo_texto(self, card, tarea, completada):
        """Sub-componente: Título y descripción (Centro)."""
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.grid(row=0, 
                        column=1, 
                        sticky="ew", 
                        padx=10, 
                        pady=6)

        txt_titulo = f"✅ {tarea['dato']}" if completada else tarea["dato"]
        estilo = "normal" if completada else "bold"
        color_texto = COLORES["texto_desc"] if completada else COLORES["texto_titulo"]

        ctk.CTkLabel(info_frame, text=txt_titulo, anchor="w",
                     font=ctk.CTkFont(size=13, weight=estilo),
                     text_color=color_texto).pack(fill="x")

        if tarea["descripcion"]:
            ctk.CTkLabel(info_frame, text=tarea["descripcion"][:60], anchor="w",
                         font=ctk.CTkFont(size=11),
                         text_color=COLORES["texto_desc"]).pack(fill="x")
    
    def _crear_acciones_tarjeta(self, card, dato, completada):
        """Sub-componente: Botones de interacción (Derecha)."""
        botones_frame = ctk.CTkFrame(card, fg_color="transparent")
        botones_frame.grid(row=0, 
                         column=2, 
                         padx=8)

        if not completada:
            self._crear_boton_icono(botones_frame,
                                    "✔", "#DCFCE7", "#16A34A",
                                    lambda: self.cmd_completar(dato))
            
        self._crear_boton_icono(botones_frame,
                                "✖", "#FEE2E2", "#DC2626",
                                lambda: self.cmd_eliminar(dato))
        

    def _crear_boton_icono(self, contenedor, icono, fondo, texto, comando):
        """Función utilitaria para generar botones de acción consistentes."""
        ctk.CTkButton(contenedor, text=icono,
                      width=34, height=34,
                      fg_color=fondo, 
                      text_color=texto,
                      command=comando).pack(side="left", padx=2)
        

    # ── Interfaces de lectura/escritura para el Controlador ──────────────────

    def obtener_datos_formulario(self):
        """Extrae el texto plano de los componentes de entrada."""
        return {
            "titulo":      self.campo_titulo.get().strip(),
            "descripcion": self.campo_descripcion.get().strip(),
            "dificultad":  self.selector_dif.get(),
        }

    def limpiar_formulario(self):
        """Restablece los componentes de entrada a su estado neutro."""
        self.campo_titulo.delete(0, "end")
        self.campo_descripcion.delete(0, "end")
        self.selector_dif.set("Media")

    def mostrar_estado(self, mensaje):
        """Modifica la cadena de texto del módulo de notificaciones."""
        self.lbl_estado.configure(text=mensaje)

    def mostrar_confirmacion(self, titulo, mensaje):
        """Invoca un cuadro de diálogo del sistema para validación booleana."""
        return messagebox.askyesno(titulo, mensaje)

    # Definición de firmas huecas (para ser sobreescritas por el Controlador)
    def cmd_agregar(self):          pass
    def cmd_completar(self, dato):  pass
    def cmd_eliminar(self, dato):   pass