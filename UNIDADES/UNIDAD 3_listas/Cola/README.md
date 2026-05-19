# Estructura de Datos: Cola (Queue) Dinámica con Nodos 

##  Concepto Fundamental

La **Cola** (*Queue*) es una estructura de datos que sigue el principio **FIFO** (*First In, First Out*):  
el primer elemento que entra es el primero en salir.

Un ejemplo cotidiano es una fila en un banco: la primera persona en llegar es la primera en ser atendida.

En esta implementación, la cola está construida usando **nodos enlazados dinámicamente**.  
Cada nodo almacena:

- Un dato.
- Una referencia al siguiente nodo.

La cola mantiene dos referencias importantes:

- **frente**: apunta al primer elemento.
- **final**: apunta al último elemento agregado.

```text
FRENTE                                     FINAL
   ↓                                         ↓
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│ 10  │ →  │ 20  │ →  │ 30  │ →  │ 40  │ → None
└─────┘    └─────┘    └─────┘    └─────┘
   ↑                                         ↑
Primero en entrar                    Último en entrar
Primero en salir                     Último en salir
```

No existen índices ni tamaño fijo; la cola crece y disminuye dinámicamente según la memoria disponible.

---

#  Implementación en Python

La implementación está dividida en tres archivos:

- `nodo.py`
- `cola.py`
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

## 📄 Archivo: `cola.py`

```python
from nodo import Nodo

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

    def encolar(self, dato):
        nuevo = Nodo(dato)

        if self.final is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

        self.tamanio += 1

    def desencolar(self):
        if self.frente is None:
            return None

        dato = self.frente.dato
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        self.tamanio -= 1
        return dato

    def ver_frente(self):
        return self.frente.dato if self.frente else None

    def esta_vacia(self):
        return self.frente is None

    def tamaño(self):
        return self.tamanio

    def mostrar(self):
        actual = self.frente

        while actual:
            print(actual.dato)
            actual = actual.siguiente
```

---

# ⏱ Análisis de Complejidad (Big O)

| Operación        | Complejidad | Explicación |
|------------------|-------------|-------------|
| `encolar()`      | `O(1)` | Solo se crea un nodo y se coloca al final. |
| `desencolar()`   | `O(1)` | El frente avanza al siguiente nodo. |
| `ver_frente()`   | `O(1)` | Acceso directo al atributo `frente`. |
| `esta_vacia()`   | `O(1)` | Solo verifica si `frente` es `None`. |
| `tamaño()`       | `O(1)` | El contador se mantiene actualizado. |
| `mostrar()`      | `O(n)` | Recorre todos los nodos de la cola. |

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
- Recorrer toda la cola requiere tiempo lineal.

---

#  Ejemplo de Uso (`main.py`)

```python
from cola import Cola

mi_cola = Cola()

mi_cola.encolar(10)
mi_cola.encolar(20)
mi_cola.encolar(30)

mi_cola.mostrar()

print(mi_cola.desencolar())

mi_cola.mostrar()

print(f"Tamaño: {mi_cola.tamaño()}")
```

---

#  Salida Esperada

```text
10
20
30

10

20
30

Tamaño: 2
```

---

#  Aplicaciones Cotidianas de una Cola

| Área | Ejemplo |
|------|----------|
| Sistemas operativos | Cola de procesos esperando CPU. |
| Impresoras | Documentos en orden de impresión. |
| Atención al cliente | Filas en bancos o supermercados. |
| Redes | Colas de paquetes de datos. |
| Simulaciones | Modelado de filas de espera. |

---

#  Diferencia entre Pila y Cola

| Característica | Pila | Cola |
|----------------|-------|-------|
| Principio | LIFO | FIFO |
| Inserción | En la cima | Al final |
| Eliminación | Desde la cima | Desde el frente |
| Referencias | `cima` | `frente` y `final` |
| Aplicaciones | Ctrl+Z, navegación | Impresión, turnos |

---

#  Posibles Mejoras Futuras

```python
# TODO: Vaciar toda la cola
# TODO: Buscar elementos
# TODO: Copiar cola
# TODO: Invertir cola
# TODO: Implementar __iter__
```

---

#  Resumen 

| Concepto | Descripción |
|----------|-------------|
| Cola | Estructura FIFO |
| Implementación | Basada en nodos enlazados |
| Inserción | Al final |
| Eliminación | Desde el frente |
| Complejidad | Operaciones principales en `O(1)` |

---

## 👨‍💻 Datos

- **Desarrollado por:** Karol Josef
- **Materia:** Estructura de Datos I
- **Semestre:** 1/2026