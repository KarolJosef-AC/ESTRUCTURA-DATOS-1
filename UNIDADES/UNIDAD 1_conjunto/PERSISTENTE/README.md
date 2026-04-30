CLASE CONJUNTO - PERSISTENTE

---

Concepto Conjunto:

Un conjunto es la agrupación organizada de elementos que comparten una o varias características comunes. Estos elementos pueden ser objetos concretos o abstractos, como números, canciones, meses, personas o planetas.

Concepto Conjunto Persistente:

Un conjunto persistente es aquel cuyo estado se guarda en un medio de almacenamiento externo, como un archivo JSON o una base de datos, de forma que sus elementos no se pierden al cerrar el programa. Al volver a ejecutarlo, el conjunto puede recuperar automáticamente los datos guardados y continuar desde donde se dejó.





Gemini dijo
Para lograr un repositorio de nivel profesional, vamos a crear tres archivos README.md específicos para cada subcarpeta de la Unidad 1. Cada uno explicará la ciencia detrás de la implementación y cómo el código que escribiste resuelve el problema.

1. README para /ESTATICO 📏
Crea este archivo en E:\...\UNIDAD 1_conjunto\ESTATICO\README.md.

Markdown
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



## 📝 Ejemplo de Uso
```python
# Crear conjunto con capacidad para 5 elementos
A = ConjuntoEstatico(capacidad_maxima=5, elementos_iniciales=[1, 2])
A.agregar(3) # Correcto
# A.agregar(4) ... hasta llenar

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

---

### 3. README para `/PERSISTENTE` 💾

Crea este archivo en `E:\...\UNIDAD 1_conjunto\PERSISTENTE\README.md`.

```markdown
# TDA Conjunto: Implementación Persistente 💾

## 🔬 Concepto Científico
La persistencia es la capacidad de una estructura de datos de **sobrevivir a la finalización del proceso** que la creó. En esta implementación, el estado del conjunto se traslada de la Memoria Volátil (RAM) al Almacenamiento Permanente (Disco HDD/SSD) utilizando el formato estándar de intercambio de datos **JSON**.

## 🛠️ Características del Código
* **Serialización:** Los datos se convierten a formato JSON mediante la librería `json`, permitiendo la interoperabilidad.
* **Sincronización Automática:** Cada operación que modifica el conjunto (`agregar`, `eliminar`) dispara un evento de guardado automático (`_guardar()`) en el disco.
* **Recuperación de Estado:** Al instanciar la clase, el constructor verifica si existe el archivo (`os.path.exists`) para restaurar los datos previos.

## 📂 Estructura de Almacenamiento
Los datos se guardan con la siguiente estructura jerárquica:
```json
{
    "elementos": [1, 2, 3, 4]
}


**Desarrollado por:** Aramayo Calle Karol Josef
**Materia:** Estructura de Datos 1  
**Semestre:** 1/2026