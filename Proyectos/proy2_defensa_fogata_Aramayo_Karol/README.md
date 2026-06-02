# Defensa de la Fogata 🔥

**Videojuego Tower Defense 2D - Proyecto Académico**

Materia: Estructura de Datos 1  
Autor: Karol Aramayo  
Lenguaje: Python 3.12 + Pygame 2.6  
Arquitectura: MVC (Model - View - Controller)
---

## 📖 Descripción

Videojuego 2D estilo Tower Defense donde el jugador debe proteger una fogata
de enemigos que avanzan hacia ella. El proyecto demuestra el uso de estructuras
de datos, POO y arquitectura MVC en un entorno interactivo.

---


---

## 🚀 Fases del Proyecto

### ✅ Fase 1 — Ventana y Game Loop
- Ventana Pygame 800×600
- Game loop a 60 FPS
- Arquitectura MVC implementada
- Archivos: `main.py`, `controlador.py`, `render.py`

### ✅ Fase 2 — Mapa y Fogata
- Grid 2D de 20×15 celdas (matriz)
- Tipos de celda: libre (0), obstáculo (1), fogata (2)
- Fogata en el centro inferior (2 celdas de ancho)
- Barra de vida sobre la fogata
- Archivos: `mapa.py`, `fogata.py`

### 🔄 Fase 3 — Enemigos *(en desarrollo)*
- Clase Enemigo con vida y velocidad
- Movimiento desde la parte superior hacia la fogata
- Daño a la fogata al llegar
- Renderizado de enemigos con barra de vida

### ⬜ Fase 4 — Estructuras de Datos
- Implementación manual de Cola (FIFO)
- Implementación manual de Lista Enlazada
- Oleadas de enemigos gestionadas con cola

### ⬜ Fase 5 — Construcciones Defensivas
- Colocación de defensas con click del mouse
- Tipos: valla, torre, muro reforzado
- Validación de posición en el grid

### ⬜ Fase 6 — Combate
- Torres disparan proyectiles
- Proyectiles dañan enemigos
- Enemigos mueren y desaparecen

### ⬜ Fase 7 — Interfaz y Pulido
- UI: oleadas, oro, puntuación
- Condiciones de victoria/derrota
- Documentación final

---

##  Instalación

```bash
# Clonar el repositorio
git clone <url-del-repo>

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt