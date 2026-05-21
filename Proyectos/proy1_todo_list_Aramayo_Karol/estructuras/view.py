import tkinter as tk
from tkinter import messagebox

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#F8FAFC")
        
        self.fuente_principal = ("Segoe UI", 11)
        self.fuente_titulo = ("Segoe UI", 20, "bold")
        
        self._construir_interfaz()

    def _construir_interfaz(self):
        self._construir_encabezado()
        self._construir_entrada()
        self._construir_botones()
        self._construir_lista()
        self._construir_estado()

    def _construir_encabezado(self):
        frame = tk.Frame(self.root, bg="#0F172A", pady=25)
        frame.pack(fill="x")

        tk.Label(
            frame, text="Gestión de Tareas", font=self.fuente_titulo,
            bg="#0F172A", fg="#F8FAFC"
        ).pack()

        tk.Label(
            frame, text="Lista Enlazada Simple", font=("Segoe UI", 10),
            bg="#0F172A", fg="#94A3B8"
        ).pack(pady=(5, 0))

    def _construir_entrada(self):
        frame = tk.Frame(self.root, bg="#F8FAFC", pady=15, padx=25)
        frame.pack(fill="x")

        self.entrada_tarea = tk.Entry(
            frame, font=("Segoe UI", 12), bd=0, highlightthickness=1,
            highlightbackground="#CBD5E1", highlightcolor="#3B82F6",
            relief="flat"
        )
        self.entrada_tarea.pack(pady=10, ipady=8, fill="x")
        self.entrada_tarea.bind("<Return>", lambda e: self.cmd_agregar())

    def _construir_botones(self):
        frame = tk.Frame(self.root, bg="#F8FAFC", padx=25)
        frame.pack(fill="x")

        botones = [
            ("Agregar", "#10B981", "cmd_agregar"),
            ("Completar", "#3B82F6", "cmd_completar"),
            ("Eliminar", "#EF4444", "cmd_eliminar"),
        ]

        fila = tk.Frame(frame, bg="#F8FAFC")
        fila.pack(pady=5, fill="x")

        for texto, bg, cmd_nombre in botones:
            btn = tk.Button(
                fila, text=texto, bg=bg, fg="white", font=("Segoe UI", 10, "bold"),
                bd=0, relief="flat", cursor="hand2", activebackground=bg, activeforeground="white",
                command=lambda c=cmd_nombre: self._ejecutar_comando(c)
            )
            btn.pack(side="left", expand=True, fill="x", padx=4, ipady=6)

    def _construir_lista(self):
        frame = tk.Frame(self.root, bg="#F8FAFC", padx=25, pady=15)
        frame.pack(fill="both", expand=True)

        contenedor = tk.Frame(frame, bg="white", bd=0, highlightthickness=1, highlightbackground="#CBD5E1")
        contenedor.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(contenedor, bd=0, relief="flat")
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            contenedor, font=("Segoe UI", 11), selectbackground="#EFF6FF", selectforeground="#1E293B",
            yscrollcommand=scrollbar.set, bd=0, relief="flat", highlightthickness=0, activestyle="none"
        )
        self.listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.config(command=self.listbox.yview)

    def _construir_estado(self):
        self.lbl_estado = tk.Label(
            self.root, text="  Sistema listo.", font=("Segoe UI", 9),
            bg="#E2E8F0", fg="#475569", anchor="w", pady=6, padx=10
        )
        self.lbl_estado.pack(fill="x", side="bottom")

    def obtener_texto_entrada(self):
        return self.entrada_tarea.get().strip()

    def limpiar_entrada(self):
        self.entrada_tarea.delete(0, tk.END)

    def actualizar_lista(self, tareas):
        self.listbox.delete(0, tk.END)
        for tarea in tareas:
            if tarea["estado"] == "completada":
                self.listbox.insert(tk.END, f"  ✓  {tarea['dato']}")
            else:
                self.listbox.insert(tk.END, f"  ○  {tarea['dato']}")
        
        for i, tarea in enumerate(tareas):
            if tarea["estado"] == "completada":
                self.listbox.itemconfig(i, fg="#94A3B8")
            else:
                self.listbox.itemconfig(i, fg="#1E293B")

    def obtener_seleccion(self):
        indices = self.listbox.curselection()
        if not indices:
            return None
        texto_completo = self.listbox.get(indices[0])
        return texto_completo.replace("  ✓  ", "").replace("  ○  ", "").strip()

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje)
        elif tipo == "advertencia":
            messagebox.showwarning(titulo, mensaje)
        else:
            messagebox.showinfo(titulo, mensaje)

    def mostrar_estado(self, mensaje):
        self.lbl_estado.config(text=f"  {mensaje}")

    def _ejecutar_comando(self, nombre):
        metodo = getattr(self, nombre, None)
        if metodo:
            metodo()

    def cmd_agregar(self):   pass
    def cmd_completar(self): pass
    def cmd_eliminar(self):  pass