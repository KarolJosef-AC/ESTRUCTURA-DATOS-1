# 📝 To-Do List — Aramayo Karol

Aplicación de lista de tareas con interfaz gráfica, construida en Python
usando el patrón **MVC** y una **lista enlazada** como estructura de datos.
La persistencia se realiza automáticamente en un archivo `tareas.json`.

---

## Datos del estudiante

| Campo    | Detalle       |
|----------|---------------|
| Nombre   | Karol Josef   |
| Apellido | Aramayo Calle |
| Grupo    | R1            |

---

## Estructura del proyecto

```
proy1_todo_list_Aramayo_Karol/
│
├── datos/
│   └── tareas.json                 # Almacenamiento automático de tareas
│
├── estructuras/
│   ├── __init__.py
│   ├── model.py                    # Nodo + ListaEnlazada (lógica de datos)
│   ├── view.py                     # Interfaz gráfica con CustomTkinter
│   └── controller.py               # Coordinación entre Model y View
│
├── main.py                         # Punto de entrada del programa
└── README.md
```

---

## Requisitos

- Python **3.10** o superior
- Biblioteca `customtkinter`

---

## Cómo ejecutar

### 1. Clonar el repositorio

```bash
git clone https://github.com/KarolJosef-AC/ESTRUCTURA-DATOS-1.git
cd "ESTRUCTURA-DATOS-1/Proyectos/proy1_todo_list_Aramayo_Karol"
```

### 2. Crear y activar entorno virtual (recomendado)

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install customtkinter
```

### 4. Ejecutar el programa

```bash
python main.py
```

---

## Funcionalidades

| Acción | Descripción | Botón |
|--------|-------------|-------|
| **Agregar** | Registra una nueva tarea con título, descripción, dificultad y categoría | ➕ |
| **Completar** | Marca una tarea como completada (solo si está pendiente) | ✔ |
| **Desmarcar** | Revierte una tarea completada a pendiente (aparece solo si está completada) | ↩ |
| **Editar** | Modifica el título y/o descripción de una tarea existente | ✏️ |
| **Eliminar** | Elimina una tarea tras confirmación del usuario | ✖ |
| **Filtrar** | Botones para filtrar tareas por categoría (Todas, Personal, Universidad, Trabajo) | 📂 |

---

## Persistencia de datos

Las tareas se guardan automáticamente en `datos/tareas.json` cada vez que se:

- ✅ Agrega una tarea
- ✅ Completa o desmarca una tarea
- ✅ Edita una tarea
- ✅ Elimina una tarea

La carpeta `datos/` y el archivo `tareas.json` se crean automáticamente la primera
vez que se ejecuta el programa; **no es necesario crearlos manualmente**.

### Ejemplo de tareas.json

```json
[
  {
    "dato": "Entregar informe",
    "descripcion": "Informe final de estructuras",
    "dificultad": "Dificil",
    "categoria": "Trabajo",
    "estado": "pendiente"
  },
  {
    "dato": "Comprar frutas",
    "descripcion": "",
    "dificultad": "Facil",
    "categoria": "Personal",
    "estado": "completada"
  },
  {
    "dato": "Estudiar para el examen",
    "descripcion": "Capítulos 1 al 5",
    "dificultad": "Media",
    "categoria": "Universidad",
    "estado": "pendiente"
  }
]
```

## Arquitectura MVC

```
main.py
  └─ Crea Vista (view.py)
  └─ Crea Controlador (controller.py)
       └─ Crea Modelo (model.py)
            └─ Lee/escribe datos/tareas.json
```

### Componentes

#### **Model (model.py)**
- Implementa la **lista enlazada simple** para almacenar tareas
- Gestiona operaciones: agregar, completar, desmarcar, editar, eliminar
- Maneja lectura y escritura del archivo `tareas.json`
- Valida que no haya duplicados de títulos
- Capacidad máxima: **100 tareas**

#### **View (view.py)**
- Construye la interfaz gráfica usando **CustomTkinter**
- Actualiza la UI cuando hay cambios en el modelo
- **No contiene lógica de negocio** (solo presentación)
- Expone métodos para que el Controlador asigne acciones

#### **Controller (controller.py)**
- Recibe eventos disparados por la Vista (clicks, formularios)
- Ejecuta la operación correspondiente en el Modelo
- Actualiza la Vista con los resultados
- Coordina la persistencia de datos

---

## Estructura de datos

Las tareas se almacenan en una **lista enlazada simple**. Cada nodo contiene:

```
┌─ Nodo ─────────────────┐
│ dato           (str)   │  ← Título de la tarea
│ descripcion    (str)   │  ← Detalle adicional
│ dificultad     (str)   │  ← "Facil" | "Media" | "Dificil"
│ categoria      (str)   │  ← "Personal" | "Universidad" | "Trabajo"
│ estado         (str)   │  ← "pendiente" | "completada"
│ siguiente      (Nodo)  │  ← Referencia al próximo nodo
└────────────────────────┘
```

### Capacidades

| Característica | Valor |
|---|---|
| Capacidad máxima | 100 tareas |
| Tipo de lista | Simple enlazada (FIFO) |
| Duplicados | No permitidos (validación por título) |
| Persistencia | JSON automático |

---


## Historial de versiones

### v1.0 (Inicial)
- Agregar tareas
- Completar tareas
- Eliminar tareas
- Filtro por categoría
- Persistencia en JSON

### v1.1 (Actual)
-  Funcionalidad de **editar** tareas
-  Funcionalidad de **desmarcar** tareas completadas
-  Arquitectura MVC mejorada
-  Interfaz visual refinada

---

## Autor

**Karol Josef Aramayo Calle**  
Grupo: R1  
Asignatura: Estructuras de Datos 1 (ED1)  
Institución: Universidad
