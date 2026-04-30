CLASE Polinomio - Arreglo
---

Concepto Polinomio:
Un polinomio es una funcion real sobre una variable, que tiene la forma:
P(x) = 3x124 + 4x11 - 8x3 + 6x - 9 donde:
Grado = 124,Coef. = 3Numero de terminos 5  ordenada de mayor a menor exponente



Concepto Polinomio - Arreglo:
Se utiliza un arreglo (vector) donde la posición A[i] almacena el coeficiente del término de grado.



# TDA Polinomio: Implementación con Arreglos (Vectores) 📊

## 🔬 Fundamento Científico
Esta implementación utiliza **memoria contigua** mediante un arreglo (lista en Python). La estructura se basa en el mapeo directo de exponentes a índices, lo que permite un acceso aleatorio de alto rendimiento.

## ⚙️ Lógica de Almacenamiento
* **Índice ($i$):** Representa el exponente del término.
* **Valor ($A[i]$):** Representa el coeficiente asociado.
* **Estado:** Un polinomio $P(x) = 1x^3 + 2x^2 + 3$ se almacena físicamente como `[3, 0, 2, 1]`.



## 🚀 Algoritmos de Alto Rendimiento
Para este modelo, se ha implementado la **Regla de Horner** en el método `evaluar(x)`. Esta técnica reduce la complejidad computacional de evaluar un polinomio de $O(n^2)$ a $O(n)$, minimizando el número de multiplicaciones requeridas:
$$P(x) = a_0 + x(a_1 + x(a_2 + \dots + x(a_{n-1} + x a_n)\dots))$$



## ⏱️ Análisis de Complejidad (Big O)
| Operación | Complejidad | Descripción |
| :--- | :--- | :--- |
| **Acceso a Coeficiente** | $O(1)$ | Acceso directo por índice de arreglo. |
| **Obtener Grado** | $O(n)$ | Requiere escanear desde el final para hallar el primer coeficiente $\neq 0$. |
| **Suma / Resta** | $O(\max(n, m))$ | Iteración lineal sobre la longitud de los arreglos. |
| **Multiplicación** | $O(n \times m)$ | Producto cruzado de todos los términos (Algoritmo de convolución). |

## ⚠️ Limitación Técnica
Esta estructura presenta baja eficiencia espacial ante **polinomios dispersos**. Un polinomio con grado 1000 y solo dos términos ocupará 1001 posiciones de memoria, la mayoría almacenando ceros.

**Desarrollado por:** Aramayo Calle Karol Josef
**Materia:** Estructura de Datos 1  
**Semestre:** 1/2026