from metodosOperaciones import Conjunto
conjunto_a = Conjunto([1, 2, 3, 4, 4, 4])
conjunto_b = Conjunto([3, 4, 5, 6])

print(f"Conjunto A: {conjunto_a}  (Cardinalidad: {len(conjunto_a)})")
print(f"Conjunto B: {conjunto_b}  (Cardinalidad: {len(conjunto_b)})")
print("-" * 43)
# Operaciones
print(f"Unión          (A ∪ B):  {conjunto_a.union(conjunto_b)}")
print(f"Intersección   (A ∩ B):  {conjunto_a.interseccion(conjunto_b)}")
print(f"Diferencia     (A \\ B):  {conjunto_a.diferencia(conjunto_b)}")
print(f"Dif. Simétrica (A △ B):  {conjunto_a.diferencia_simetrica(conjunto_b)}")
print("-" * 43)
conjunto_a.eliminar(3)
print(f"A tras eliminar 3: {conjunto_a}")
# conjunto vacio
conjunto_vacio = Conjunto()
print(f"Conjunto vacío: {conjunto_vacio}")