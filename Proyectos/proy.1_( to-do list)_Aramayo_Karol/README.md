# To-Do List — Aramayo Karol

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
pro1_(todo lista)aramayo karol/
│
├── datos/
│   └── tareas.json          # Almacenamiento automático de tareas
│
├── estructuras/
│   ├── model.py             # Nodo + ListaEnlazada (lógica de datos)
│   ├── view.py              # Interfaz gráfica con CustomTkinter
│   └── controller.py        # Coordinación entre Model y View
│
├── main.py                  # Punto de entrada del programa
└── README.md
```

---

## Requisitos

- Python **3.10** o superior
- Biblioteca `customtkinter`

---

## Cómo ejecutar

### 1. Clonar el repositorio
El sistema Git descargará la estructura completa de la materia. Se debe ejecutar el siguiente comando en la terminal:

```bash
git clone [https://github.com/KarolJosef-AC/ESTRUCTURA-DATOS-1.git](https://github.com/KarolJosef-AC/ESTRUCTURA-DATOS-1.git)


cd "ESTRUCTURA-DATOS-1/Proyectos/proy.1_( to-do list)_Aramayo_Karol"
```

### 2. Instalar dependencias

```bash
pip install customtkinter
```

### 3. Ejecutar el programa

```bash
python main.py
```

> En Windows también puede ejecutarse haciendo doble clic en `main.py`
> si Python está asociado a archivos `.py`.

---

## Funcionalidades

| Acción | Descripción |
|---|---|
| **Agregar** | Registra una nueva tarea con título, descripción, fecha, dificultad y categoría |
| **Completar** | Marca una tarea existente como completada |
| **Eliminar** | Elimina una tarea tras confirmación del usuario |
| **Filtrar** | Muestra tareas por categoría (Todas, Estudio, Personal, Trabajo) |

---

## Persistencia de datos

Las tareas se guardan automáticamente en `datos/tareas.json` cada vez
que se agrega, completa o elimina una tarea.

La carpeta `datos/` y el archivo `tareas.json` se crean solos la primera
vez que se ejecuta el programa; no es necesario crearlos manualmente.

### Ejemplo de `tareas.json`

```json
[
  {
    "dato": "Entregar informe",
    "descripcion": "Informe final de estructuras",
    "fecha_entrega": "2025-05-10",
    "dificultad": "Dificil",
    "categoria": "Trabajo",
    "estado": "pendiente"
  },
  {
    "dato": "Comprar frutas",
    "descripcion": "",
    "fecha_entrega": "",
    "dificultad": "Facil",
    "categoria": "Personal",
    "estado": "completada"
  }
]
```

> Para **reiniciar** todas las tareas, basta con borrar el contenido de
> `tareas.json` o eliminar el archivo. Se regenerará vacío al iniciar.

---

## Arquitectura MVC

```
main.py
  └── crea Vista (view.py)
  └── crea Controlador (controller.py)
        └── crea Modelo (model.py)
              └── lee/escribe datos/tareas.json
```

- **Model** (`model.py`): implementa la lista enlazada. Gestiona las
  operaciones sobre los nodos y la lectura/escritura del JSON.
- **View** (`view.py`): construye y actualiza la interfaz gráfica.
  No contiene lógica de negocio.
- **Controller** (`controller.py`): recibe eventos de la Vista, llama
  al Modelo y actualiza la Vista con los resultados.

---

## Estructura de datos

Las tareas se almacenan en una **lista enlazada simple**. Cada nodo
contiene:

```
Nodo
 ├── dato           (título de la tarea)
 ├── descripcion
 ├── fecha_entrega
 ├── dificultad     ("Facil" | "Media" | "Dificil")
 ├── categoria      ("Estudio" | "Personal" | "Trabajo")
 ├── estado         ("pendiente" | "completada")
 └── siguiente      → Nodo | None
```

La lista tiene una capacidad máxima de **100 tareas**.
