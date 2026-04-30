CLASE POLINOMIO - LISTA ENLAZADAS

Concepto POLINOMIO:

Concepto Polinomio: Un polinomio es una funcion real sobre una variable, que tiene la forma: P(x) = 3x124 + 4x11 - 8x3 + 6x - 9 donde: Grado = 124,Coef. = 3Numero de terminos 5 ordenada de mayor a menor exponente

Concepto POLINOMIO - Lista Enlazada:

Un polinomio representado mediante listas enlazadas es una estructura de datos dinámica donde cada nodo almacena un término del polinomio, compuesto por coeficiente, exponente y un puntero al siguiente término.



# TDA Polinomio: Implementación con Listas Enlazadas 🔗

## 🔬 Fundamento Científico
Esta implementación utiliza **asignación dinámica de memoria**. Cada término del polinomio se representa como un `NodoPolinomio` independiente, permitiendo que la estructura crezca o decrezca según la necesidad algorítmica.

## ⚙️ Estructura del Nodo
Cada entidad en la secuencia topológica contiene:
1. **Coeficiente:** Valor escalar del término.
2. **Exponente:** Potencia de la variable.
3. **Siguiente:** Puntero/Referencia a la dirección de memoria del próximo término.



## 🛠️ Innovaciones en el Código
* **Inserción Ordenada:** El método `agregar_termino()` garantiza que la lista se mantenga siempre de mayor a menor exponente, optimizando las operaciones de suma y división.
* **Contracción Topológica:** Se incluyó el método `simplificar()` para desintegrar nodos con coeficientes nulos, manteniendo la precisión del grado del polinomio.
* **Superposición:** En caso de insertar un exponente existente, se aplica la suma algebraica automática de coeficientes.



## ⏱️ Análisis de Complejidad (Big O)
| Operación | Complejidad | Descripción |
| :--- | :--- | :--- |
| **Obtener Grado** | $O(1)$ | El mayor exponente siempre reside en el nodo `cabeza`. |
| **Acceso a Coeficiente** | $O(k)$ | Requiere un recorrido secuencial hasta encontrar el exponente ($k = \text{términos no nulos}$). |
| **Memoria** | $O(k)$ | Consumo de memoria proporcional únicamente a los términos existentes. |

## 💡 Ventaja en Polinomios Dispersos
Es la estructura de oro para la **Ingeniería de Sistemas**, ya que permite representar polinomios de grados altísimos (ej. $x^{1000000} + 1$) consumiendo únicamente la memoria de dos nodos, eliminando el desperdicio de espacio.


**Desarrollado por:** Aramayo Calle Karol Josef
**Materia:** Estructura de Datos 1  
**Semestre:** 1/2026