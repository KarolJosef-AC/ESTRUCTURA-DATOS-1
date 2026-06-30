# Defensa de la Fogata 🔥
## Videojuego Tower Defense 2D - Proyecto Académico

| Campo | Descripción |
|--------|-------------|
| **Materia** | Estructura de Datos 1 (INF-220) |
| **Autor** | Karol Aramayo |
| **Lenguaje** | Python 3.12 + Pygame 2.6 |
| **Arquitectura** | MVC (Model - View - Controller) |
| **Ventana** | 1000×670 px (800 mapa + 200 panel) |

---

# 📖 Descripción

Protege la fogata de criaturas que bajan desde lo alto. Coloca **vallas**, **torres** y **muros** para detenerlas antes de que lleguen al objetivo. Las torres disparan automáticamente y los enemigos intentarán abrirse paso destruyendo las defensas.

El objetivo es sobrevivir la mayor cantidad de oleadas posible mientras administras correctamente tus recursos.

Este proyecto demuestra el uso de **estructuras de datos implementadas desde cero**, sin utilizar implementaciones equivalentes de la biblioteca estándar de Python.

Las estructuras utilizadas son:

- Cola (FIFO)
- Lista Enlazada
- Tabla Hash
- Matriz 2D
- Planificador de Procesos (Scheduler por prioridad)

---

# 🎮 Controles

| Tecla | Acción |
|--------|--------|
| **1** | Seleccionar Valla (20 oro) |
| **2** | Seleccionar Torre (50 oro) |
| **3** | Seleccionar Muro (30 oro) |
| **Click Izquierdo** | Colocar defensa |
| **P** | Pausar / Reanudar |
| **ESC** | Volver al menú principal |
| **R** | Reiniciar partida (Game Over) |

---

# 🧩 Entidades del Juego

## 👾 Enemigos

| Tipo | Vida | Velocidad | Color | Comportamiento |
|------|------|-----------|--------|----------------|
| Normal | 45 HP | 0.8 | Rojo | Esquiva obstáculos |
| Tanque | 80 HP | 0.6 | Púrpura | No esquiva, daño ×3 |
| Rápido | 25 HP | 1.4 | Morado | Muy veloz, aparece cada 3 oleadas |

---

## 🛡️ Defensas

| Tipo | Vida | Costo | Función |
|------|------|-------|----------|
| Valla | 40 HP | 20 oro | Bloquea enemigos |
| Torre | 30 HP | 50 oro | Dispara proyectiles (15 daño) |
| Muro | 80 HP | 30 oro | Alta resistencia |

---

## 🔥 Fogata

- **Posición:** Columnas 9 y 10 de la última fila.
- **Vida inicial:** 100 HP.
- Cada enemigo que llega causa **10 HP** de daño.

---

# 📚 Estructuras de Datos Utilizadas

| Estructura | Archivo | Uso | Complejidad |
|------------|---------|-----|-------------|
| Matriz 2D | `mapa.py` | Representación del mapa (20×15) | O(1) acceso |
| Cola FIFO | `cola.py` | Administración de oleadas | O(1) encolar/desencolar |
| Lista Enlazada | `lista_enlazada.py` | Enemigos activos | O(1) eliminación por referencia |
| Tabla Hash | `tabla_hash.py` | Puntuaciones y persistencia JSON | O(1) promedio |
| Planificador | `planificador.py` | Orden de ejecución de acciones | O(n) registro |

---

# 📁 Estructura del Proyecto

```text
src/
├── main.py                          # Punto de entrada
│
├── controller/
│   └── controlador.py               # Game Loop y coordinación
│
├── model/
│   ├── mapa.py                      # Matriz del mapa
│   ├── logica_juego.py              # Lógica principal
│   │
│   ├── entidades/
│   │   ├── enemigo.py
│   │   ├── defensa.py
│   │   ├── fogata.py
│   │   └── proyectil.py
│   │
│   └── estructuras/
│       ├── cola.py
│       ├── lista_enlazada.py
│       ├── planificador.py
│       └── tabla_hash.py
│
└── view/
    └── render.py                    # Renderizado con Pygame
```

---

# 🔧 Instalación

```bash
# Clonar repositorio
git clone https://github.com/KarolJosef-AC/ESTRUCTURA-DATOS-1.git

cd ESTRUCTURA-DATOS-1/Proyectos/proy2_defensa_fogata_Aramayo_Karol

# Crear entorno virtual
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install pygame

# Ejecutar
python src/main.py
```

---

# 🎯 Características Técnicas

- Arquitectura MVC estricta.
- Implementación manual de estructuras de datos.
- Sin utilizar `collections.deque`.
- Sin utilizar `dict` como implementación de la tabla hash.
- Planificador de procesos basado en prioridades.
- Panel lateral con el estado del scheduler en tiempo real.
- Persistencia de puntuaciones mediante JSON.
- Código documentado mediante docstrings.
- Única dependencia externa: **Pygame**.

---

# 📊 Panel del Planificador

El panel lateral de **200 px** muestra en tiempo real:

- Últimas acciones ejecutadas.
- Prioridad de cada acción.
- Separadores entre frames.
- Auto-scroll hacia las acciones más recientes.

### Colores

| Color | Prioridad |
|--------|-----------|
| 🔴 Rojo | Crítico |
| 🟠 Naranja | Alto |
| 🔵 Azul | Normal |
| ⚪ Gris | Bajo |

---

# 🏗️ Arquitectura MVC

```text
                    CONTROLADOR
                (controlador.py)
                      │
          Recibe entradas del usuario
                      │
      Registra acciones en el Planificador
                      │
        Coordina Modelo y Vista del juego
              ┌──────────────┴──────────────┐
              ▼                             ▼
          MODELO                         VISTA
                                         render.py
              │
      ├── mapa.py
      ├── logica_juego.py
      ├── enemigo.py
      ├── defensa.py
      ├── fogata.py
      ├── proyectil.py
      ├── cola.py
      ├── lista_enlazada.py
      ├── planificador.py
      └── tabla_hash.py
```

---

# 📌 Objetivos Académicos

Este proyecto fue desarrollado para demostrar la aplicación práctica de los contenidos de la materia **Estructura de Datos I**, implementando estructuras fundamentales desde cero e integrándolas en un videojuego funcional desarrollado con **Python** y **Pygame**.

Se aplican conceptos como:

- Matrices bidimensionales.
- Listas enlazadas.
- Colas FIFO.
- Tablas Hash.
- Planificación por prioridad.
- Arquitectura MVC.
- Programación orientada a objetos.
- Persistencia de datos mediante JSON.

---
**Autor:** Karol Aramayo  
**Materia:** Estructura de Datos I (INF-220)