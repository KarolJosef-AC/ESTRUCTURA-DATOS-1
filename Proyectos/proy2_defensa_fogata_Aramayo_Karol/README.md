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

### ✅ Fase 3 — Enemigos
- Clase Enemigo con vida y velocidad
- Movimiento desde la parte superior hacia la fogata
- Daño a la fogata al llegar
- Renderizado de enemigos con barra de vida

### ✅ Fase 4 — Estructuras de Datos
- Implementación manual de Cola (FIFO) en `cola.py`
- Implementación manual de Lista Enlazada en `lista_enlazada.py`
- Oleadas de enemigos gestionadas con cola
- Enemigos activos almacenados en lista enlazada
- Archivos: `cola.py`, `lista_enlazada.py`

### ✅ Fase 5 — Construcciones Defensivas
- Colocación de defensas con click del mouse
- Tipos: valla, torre, muro
- Validación de posición en el grid
- Enemigos bloqueados por defensas
- Enemigos dañan y destruyen defensas
- Archivos: `defensa.py`

### ✅ Fase 6 — Combate
- Torres disparan proyectiles automáticamente
- Proyectiles persiguen al enemigo más cercano
- Enemigos reciben daño y mueren
- Archivos: `proyectil.py`

### ✅ Fase 7 — Interfaz y Fin de Juego
- Contador de oleadas y puntuación en pantalla
- Condición de victoria: sobrevivir 5 oleadas
- Condición de derrota: la fogata se destruye
- Pantalla de Game Over / Victoria
- Reinicio con tecla R

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