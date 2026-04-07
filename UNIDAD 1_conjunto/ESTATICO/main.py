from metodosoperaciones import ConjuntoEstatico

a = ConjuntoEstatico(5, [1, 2, 3])
b = ConjuntoEstatico(5, [3, 4, 5])
u = ConjuntoEstatico(10, [1, 2, 3, 4, 5, 6, 7])

print(f"A:            {a}  (capacidad: {a.capacidad_maxima})")
print(f"B:            {b}  (capacidad: {b.capacidad_maxima})")
print(f"¿A lleno?     {a.esta_lleno()}")
print("-" * 40)
print(f"A ∪ B:        {a.union(b)}")
print(f"A ∩ B:        {a.interseccion(b)}")
print(f"A \\ B:        {a.diferencia(b)}")
print(f"A':           {a.complemento(u)}")
print(f"¿Disjuntos?   {a.son_disjuntos(b)}")
print("-" * 40)

# Error esperado — conjunto lleno
a_lleno = ConjuntoEstatico(3, [1, 2, 3])
try:
    a_lleno.agregar(4)
except OverflowError as e:
    print(f"[OverflowError] {e}")