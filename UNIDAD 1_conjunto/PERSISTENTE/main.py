from metodosOperaciones import ConjuntoPersistente


a = ConjuntoPersistente("conjunto_a", [1, 2, 3, 4])
b = ConjuntoPersistente("conjunto_b", [3, 4, 5, 6])
u = ConjuntoPersistente("conjunto_u", [1, 2, 3, 4, 5, 6, 7, 8])

print(f"A: {a}  (cardinalidad: {len(a)})")
print(f"B: {b}")
print("-" * 40)
print(f"A ∪ B:       {a.union(b)}")
print(f"A ∩ B:       {a.interseccion(b)}")
print(f"A \\ B:       {a.diferencia(b)}")
print(f"A':          {a.complemento(u)}")
print(f"¿Disjuntos?  {a.son_disjuntos(b)}")
print("-" * 40)

# Modificar y verificar que se guarda
a.agregar(99)
print(f"A tras agregar 99:   {a}")
a.eliminar(99)
print(f"A tras eliminar 99:  {a}")
print("-" * 40)

# Segunda ejecución: carga automáticamente desde los archivos
a2 = ConjuntoPersistente("conjunto_a")
print(f"A recuperado desde disco: {a2}")
print("-" * 40)

# Limpieza de archivos
a.eliminar_archivo()
b.eliminar_archivo()
u.eliminar_archivo()
a.union(b).eliminar_archivo()
a.interseccion(b).eliminar_archivo()
a.diferencia(b).eliminar_archivo()