CLASE CONJUNTO - ESTATICO
---

Concepto Conjunto:

Un conjunto es la agrupación organizada de elementos que comparten una o varias características comunes. Estos elementos pueden ser objetos concretos o abstractos, como números, canciones, meses, personas o planetas.

Concepto Conjunto Estatico:

Un conjunto estático es aquel cuya capacidad máxima se define en el momento de su creación y no puede ser modificada. Una vez que alcanza ese límite, no es posible agregar más elementos, lo que garantiza un uso de memoria fijo y predecible durante toda la ejecución del programa.


---



# TDA Conjunto: Implementación Estática 📏

## 🔬 Concepto Científico
La implementación estática se basa en el uso de **memoria contigua** y preasignada. En esta variante, el conjunto tiene un límite físico definido desde su nacimiento (Capacidad Máxima), lo que refleja cómo se comportan las estructuras en lenguajes de bajo nivel como C o C++.

## 🛠️ Características del Código
* **Gestión de Memoria:** Utiliza una lista de Python pero restringida por el atributo `self.capacidad_maxima`.
* **Control de Errores:** Implementa `OverflowError` para evitar el desbordamiento de la estructura si se intenta agregar más elementos de los permitidos.
* **Tipado Fuerte:** Valida que solo se ingresen números enteros (`isinstance(int)`), asegurando la homogeneidad de los datos.

## 📊 Eficiencia y Limitaciones
| Aspecto | Detalle |
| :--- | :--- |
| **Ventaja** | Predictibilidad del uso de memoria en hardware limitado. |
| **Desventaja** | Inflexible. Si el conjunto crece, se requiere crear uno nuevo. |
| **Operación Crítica** | `agregar()` verifica `esta_lleno()` antes de cada inserción ($O(n)$). |

[Image of fixed size array memory allocation]

## 📝 Ejemplo de Uso
```python
# Crear conjunto con capacidad para 5 elementos
A = ConjuntoEstatico(capacidad_maxima=5, elementos_iniciales=[1, 2])
A.agregar(3) # Correcto
# A.agregar(4) ... hasta llenar


**Desarrollado por:** Aramayo Calle Karol Josef
**Materia:** Estructura de Datos 1  
**Semestre:** 1/2026