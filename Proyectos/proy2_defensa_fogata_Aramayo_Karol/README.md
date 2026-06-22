# Defensa de la Fogata 🔥

**Videojuego Tower Defense 2D - Proyecto Académico**

Materia: Estructura de Datos 1  
Autor: Karol Aramayo  
Lenguaje: Python 3.12 + Pygame 2.6  
Arquitectura: MVC (Model - View - Controller)

---

## 📖 Descripción

Protege la fogata de criaturas que bajan desde lo alto. Colocá vallas, torres y muros
para detenerlas. Las torres disparan automáticamente. Sobreviví la mayor cantidad de
oleadas posible.

El proyecto demuestra el uso de **Cola**, **Lista Enlazada**, **Tabla Hash** y **Matriz 2D**
implementadas desde cero, junto con POO y arquitectura MVC.

---

## 🎮 Controles

| Tecla | Acción |
|-------|--------|
| `1` `2` `3` | Seleccionar defensa (valla, torre, muro) |
| Click | Colocar defensa en celda libre |
| `P` | Pausar / Reanudar |
| `ESC` | Volver al menú principal |
| `R` | Reiniciar al terminar |

---

## 📚 Estructuras de Datos

| Estructura | Uso en el juego |
|------------|-----------------|
| Matriz 2D | Mapa de 20×15 celdas |
| Cola (FIFO) | Oleadas de enemigos esperando |
| Lista Enlazada | Enemigos activos en pantalla |
| Tabla Hash | Puntuaciones guardadas en JSON |

---

## 🔧 Instalación

```bash
git clone https://github.com/KarolJosef-AC/ESTRUCTURA-DATOS-1.git
cd Proyectos/proy2_defensa_fogata_Aramayo_Karol
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt