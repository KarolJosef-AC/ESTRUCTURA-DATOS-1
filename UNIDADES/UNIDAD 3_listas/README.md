# Unidad 3: Tipo de Dato Abstracto (TDA) Lista 📜

## 🎯 Objetivo General
Definir, analizar e implementar el Tipo de Dato Abstracto **Lista**, explorando las distintas topologías de asignación de memoria (contigua y dinámica) y evaluando su impacto en la complejidad computacional para la manipulación de colecciones de datos secuenciales.

---

## 🔬 Fundamentos Teóricos
En ciencias de la computación, una **Lista** es una colección secuencial y ordenada de elementos. A diferencia del TDA Conjunto, en una lista **sí importa el orden** posicional de los elementos y **se permiten duplicados**. 

La representación de este modelo matemático en el hardware de una computadora se divide en dos grandes paradigmas de gestión de memoria:

1. **Memoria Contigua (Listas Secuenciales / Arreglos):** Los elementos ocupan bloques de memoria física adyacentes. El acceso es calculable mediante aritmética de punteros, pero su tamaño suele ser fijo, lo que provoca ineficiencia al crecer.
2. **Memoria Dinámica (Listas Enlazadas):** Los elementos (Nodos) están dispersos en la memoria física y se unifican lógicamente mediante referencias (punteros). Crece y decrece bajo demanda exacta, previniendo el desperdicio de RAM.

---

## 🗂️ Taxonomía Estructural (Variantes Implementadas)

El TDA Lista se bifurca en múltiples topologías dependiendo de la necesidad algorítmica.

### 1. Lista Secuencial (Basada en Arreglos)
* **Estructura:** Uso de índices para la ubicación espacial.
* **Ventaja:** Acceso directo $O(1)$ a cualquier posición $i$.
* **Desventaja:** Las operaciones de inserción y eliminación en posiciones intermedias exigen el desplazamiento masivo de los elementos subyacentes ($O(n)$).

### 2. Lista Simple Enlazada (Singly Linked List) 🔗
* **Estructura:** Colección unidireccional. Cada nodo almacena un dato y una única referencia al nodo sucesor.
* **Flujo:** $\text{Cabeza} \rightarrow \text{Nodo}_1 \rightarrow \dots \rightarrow \text{Cola} \rightarrow \text{Null}$
* **Aplicación:** Ideal para implementaciones de Pilas (Stacks) y manipulación rápida de datos en los extremos.

### 3. Lista Doblemente Enlazada (Doubly Linked List) ⛓️
* **Estructura:** Colección bidireccional. Cada nodo almacena un dato, una referencia al nodo sucesor y una referencia al nodo antecesor.
* **Flujo:** $\text{Null} \leftarrow \text{Nodo}_A \rightleftarrows \text{Nodo}_B \rightarrow \text{Null}$
* **Aplicación:** Permite la iteración en reverso y la eliminación de nodos en $O(1)$ si se conoce su dirección, a costa de un mayor consumo de memoria (overhead por el puntero extra).

### 4. Lista Circular (Circular Linked List) 🔄
* **Estructura:** El último nodo de la colección no apunta a nulo, sino que redirige su puntero `siguiente` hacia el nodo cabecera, cerrando el ciclo.
* **Aplicación:** Sistemas de turnos, planificación de procesos en sistemas operativos (Round-Robin) y buffers de transmisión de datos.

---

## ⏱️ Análisis de Complejidad Algorítmica (Big O)

Comparativa del rendimiento espaciotemporal en el peor de los casos (Worst-Case Scenario) entre los dos paradigmas principales:

| Operación | Secuencial (Arreglo) | Simple Enlazada | Doble Enlazada |
| :--- | :---: | :---: | :---: |
| **Acceso a índice $i$**| $O(1)$ | $O(n)$ | $O(n)$ |
| **Inserción al inicio** | $O(n)$ | $O(1)$ | $O(1)$ |
| **Inserción al final** | $O(1)$ amortizado | $O(1)$ * | $O(1)$ * |
| **Búsqueda por valor** | $O(n)$ | $O(n)$ | $O(n)$ |
| **Eliminación inicial** | $O(n)$ | $O(1)$ | $O(1)$ |
| **Sobrecarga de Memoria**| Nula | Media (1 puntero) | Alta (2 punteros) |

*\* Suponiendo que la estructura mantiene un puntero de referencia hacia la `cola`.*

---

## 🛠️ Estándares de Calidad y Robustez

El código fuente presente en este repositorio ha sido desarrollado bajo estrictos estándares científicos y de sintaxis:

* **Control de Excepciones de Hardware:** * Se mitiga el **Overflow** (Agotamiento de RAM) interceptando la excepción `MemoryError` durante la instanciación de nuevos nodos.
  * Se mitiga el **Underflow** mediante validaciones preventivas de estado nulo (`vacia()`) antes de cualquier operación de sustracción topológica.
* **Diseño Conciso y Encapsulamiento:** Aplicación de verbos de acción única (`anteponer`, `anexar`, `extraer`, `truncar`) para métodos, reduciendo la ambigüedad lógica.
* **Conformidad PEP 8:** El código obedece las convenciones de estilo de Python, incluyendo el uso exclusivo de caracteres ASCII en identificadores (sustitución de la variable `tamaño` por `total` o `longitud`) y la verificación de identidades en memoria mediante el operador `is`.

---
**Desarrollado por:** Aramayo Calle Karol Josef
**Materia:** Estructura de Datos 1  
**Periodo Académico:** 1/2026
