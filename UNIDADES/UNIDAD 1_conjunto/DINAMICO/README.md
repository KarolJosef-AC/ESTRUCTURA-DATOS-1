
CLASE CONJUNTO - DINAMICA
Concepto Conjunto:

Un conjunto es la agrupación organizada de elementos que comparten una o varias características comunes. Estos elementos pueden ser objetos concretos o abstractos, como números, canciones, meses, personas o planetas.

Concepto Conjunto Dinamico:

Un conjunto dinámico es aquel cuyo tamaño no está fijado de antemano: puede crecer agregando nuevos elementos o reducirse eliminando los existentes durante la ejecución del programa, sin ningún límite predefinido de capacidad.




---

### 2. README para `/DINAMICO` 🚀

Crea este archivo en `E:\...\UNIDAD 1_conjunto\DINAMICO\README.md`.

```markdown
# TDA Conjunto: Implementación Dinámica 🚀

## 🔬 Concepto Científico
A diferencia de la estática, la implementación dinámica utiliza **asignación de memoria bajo demanda**. El conjunto no tiene un límite arbitrario; crece proporcionalmente a la cantidad de datos recibidos, optimizando el uso de recursos cuando la cardinalidad es desconocida.

## 🛠️ Características del Código
* **Extensibilidad:** Basado en la herencia de una clase base para separar la estructura (`clase.py`) de la lógica de negocio (`metodosOperaciones.py`).
* **Axioma de Extensionalidad:** Implementado en el método `agregar()`, garantizando que cada elemento sea único mediante la verificación de membresía antes de la inserción.
* **Abstracción:** Uso de métodos mágicos (`__len__`, `__str__`) para que el objeto se comporte como una estructura nativa de Python.

## 📐 Operaciones de Álgebra de Conjuntos
Este módulo incluye la implementación lógica completa:
* **Unión ($A \cup B$):** Fusión de elementos sin repetición.
* **Intersección ($A \cap B$):** Selección de elementos comunes.
* **Diferencia Simétrica ($A \Delta B$):** Implementada científicamente como `(A ∪ B) - (A ∩ B)`.



## 📝 Ejemplo de Uso
```python
A = Conjunto([1, 2, 3])
B = Conjunto([3, 4, 5])
C = A.union(B) # Resultado: {1, 2, 3, 4, 5}

**Desarrollado por:** Aramayo Calle Karol Josef
**Materia:** Estructura de Datos 1  
**Semestre:** 1/2026