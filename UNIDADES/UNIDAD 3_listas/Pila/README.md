# Estructura de Datos: Pila (Stack) Dinámica con Nodos 

##  Concepto Fundamental

La **Pila** (*Stack*) es una estructura de datos que sigue el principio **LIFO** (*Last In, First Out*):  
el último elemento que entra es el primero en salir.

Un ejemplo cotidiano es una torre de platos: solo puedes agregar o quitar el plato que está arriba.

En esta implementación, la pila está construida usando **nodos enlazados dinámicamente**.  
Cada nodo almacena:

- Un dato.
- Una referencia al siguiente nodo.

La **cima** (tope) siempre apunta al nodo más reciente.

```text
TOPE (cima)
   ↓
┌─────┐    ┌─────┐    ┌─────┐
│ 30  │ →  │ 20  │ →  │ 10  │ → None
└─────┘    └─────┘    └─────┘
   ↑                         ↑
Último en entrar      Primero en entrar
```

No existen índices ni tamaño fijo; la pila crece y disminuye dinámicamente según la memoria disponible.

---

#  Implementación en Python

La implementación está dividida en tres archivos:

- `nodo.py`
- `pila.py`
- `main.py`

---

## 📄 Archivo: `nodo.py`

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
```

---

## 📄 Archivo: `pila.py`

```python
from nodo import Nodo

class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo
        self.tamanio += 1

    def desapilar(self):
        if self.cima is None:
            return None

        dato = self.cima.dato
        self.cima = self.cima.siguiente
        self.tamanio -= 1
        return dato

    def ver_cima(self):
        return self.cima.dato if self.cima else None

    def esta_vacia(self):
        return self.cima is None

    def tamaño(self):
        return self.tamanio

    def mostrar(self):
        actual = self.cima

        while actual:
            print(actual.dato)
            actual = actual.siguiente
```

---

# ⏱ Análisis de Complejidad (Big O)

| Operación        | Complejidad | Explicación |
|------------------|-------------|-------------|
| `apilar()`       | `O(1)` | Solo se crea un nodo y se coloca en la cima. |
| `desapilar()`    | `O(1)` | La cima avanza al siguiente nodo. |
| `ver_cima()`     | `O(1)` | Acceso directo al atributo `cima`. |
| `esta_vacia()`   | `O(1)` | Solo verifica si `cima` es `None`. |
| `tamaño()`       | `O(1)` | El contador se mantiene actualizado. |
| `mostrar()`      | `O(n)` | Recorre todos los nodos de la pila. |

---

#  Ventajas y Desventajas

## ✅ Ventajas

- Tamaño dinámico.
- Inserciones y eliminaciones rápidas.
- No desperdicia memoria innecesaria.
- Implementación sencilla.

## ❌ Desventajas

- No hay acceso directo a elementos internos.
- Cada nodo usa memoria extra para el puntero.
- Recorrer toda la pila requiere tiempo lineal.

---

#  Ejemplo de Uso (`main.py`)

```python
from pila import Pila

mi_pila = Pila()

mi_pila.apilar(10)
mi_pila.apilar(20)
mi_pila.apilar(30)

mi_pila.mostrar()

print(mi_pila.desapilar())

mi_pila.mostrar()

print(f"Tamaño: {mi_pila.tamaño()}")
```

---

#  Salida Esperada

```text
30
20
10

30

20
10

Tamaño: 2
```

---

#  Aplicaciones Cotidianas de una Pila

| Área | Ejemplo |
|------|----------|
| Editores de texto | `Ctrl + Z` (Deshacer). |
| Navegadores web | Botón "Atrás". |
| Llamadas a funciones | Pila de ejecución del sistema. |
| Evaluación matemática | Resolución de expresiones con paréntesis. |
| Validación | Balanceo de símbolos `() [] {}`. |

---

#  Diferencia entre Pila Dinámica y Pila Estática

| Característica | Pila Dinámica | Pila Estática |
|----------------|---------------|----------------|
| Tamaño | Variable | Fijo |
| Memoria | Se asigna por nodo | Bloque contiguo |
| Riesgo | Depende de RAM | Puede desbordarse |
| Inserción/Eliminación | `O(1)` | `O(1)` |

---

#  Posibles Mejoras Futuras

```python
# TODO: Vaciar toda la pila
# TODO: Buscar elementos
# TODO: Copiar pila
# TODO: Invertir pila
# TODO: Implementar __iter__
```

---



#  Resumen 

| Concepto | Descripción |
|----------|-------------|
| Pila | Estructura LIFO |
| Implementación | Basada en nodos enlazados |
| Inserción | En la cima |
| Eliminación | Desde la cima |
| Complejidad | Operaciones principales en `O(1)` |

---

## 👨‍💻 Datos

- **Desarrollado por:** Karol Josef
- **Materia:** Estructura de Datos I
- **Semestre:** 1/2026