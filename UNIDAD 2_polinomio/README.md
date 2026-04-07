

# Unidad 1: El TDA Conjunto (Set) 🎯

## Objetivo
Implementar el Tipo de Dato Abstracto (TDA) **Conjunto**, fundamentado en la teoría matemática de conjuntos, garantizando el cumplimiento de sus axiomas básicos en un entorno de programación imperativa con Python.

---

## 1. Fundamentos Teóricos
Un **Conjunto** es una colección de objetos bien definidos y diferenciables, llamados elementos. En computación, se define bajo dos reglas críticas:

* **Axioma de Extensionalidad:** No existen elementos duplicados. $A = \{1, 2, 2\}$ es incorrecto; lo correcto es $A = \{1, 2\}$.
* **No Orden:** La posición de los elementos no altera al conjunto. $\{1, 2\} = \{2, 1\}$.

---

## 2. Operaciones Lógicas (Álgebra de Conjuntos)

| Operación | Notación | Descripción Científica | Complejidad ($O$) |
| :--- | :--- | :--- | :--- |
| **Pertenencia** | $x \in A$ | Verifica si un elemento existe en la estructura. | $O(n)$ |
| **Unión** | $A \cup B$ | Elementos que están en $A$, en $B$ o en ambos. | $O(n + m)$ |
| **Intersección** | $A \cap B$ | Elementos comunes presentes en ambos conjuntos. | $O(n \times m)$ |
| **Diferencia** | $A - B$ | Elementos que pertenecen a $A$ pero no a $B$. | $O(n \times m)$ |
| **Dif. Simétrica** | $A \Delta B$ | $(A \cup B) - (A \cap B)$. Elementos no comunes. | $O(n \times m)$ |

---

## 3. Implementaciones del Repositorio

### 3.1 Clase Estática (/ESTATICO)
* **Memoria:** Preasignada (Array de tamaño fijo).
* **Ventaja:** Acceso rápido y control total del hardware.
* **Desventaja:** Riesgo de *Overflow* si se supera la capacidad inicial.

### 3.2 Clase Dinámica (/DINAMICO)
* **Memoria:** Asignación en tiempo de ejecución (Listas ligadas o dinámicas).
* **Ventaja:** El conjunto crece según la necesidad de los datos.

### 3.3 Clase Permanente (/PERSISTENTE)
* **Memoria:** Almacenamiento en archivos físicos (.txt o .dat).
* **Ventaja:** Los datos sobreviven al cierre del programa (Persistencia).

---

## 4. Estándares de Implementación en Python
Para asegurar la calidad del código, se han seguido las siguientes reglas de ingeniería:

* **Encapsulamiento:** El atributo `self.elementos` contiene la estructura interna.
* **Métodos Mágicos:** * `len`: Para obtener la cardinalidad mediante `len(conjunto)`.
    * `str`: Para visualizar el conjunto con formato matemático `{a, b, c}`.
* **Validación de Extensionalidad:** El método `agregar()` siempre verifica la preexistencia del dato.

---
