from operaciones import PolinomioArreglo

p1 = PolinomioArreglo([3, 0, 2, 1])    # Representa: 1x³ + 2x² + 3
p2 = PolinomioArreglo([1, 2, 1])       # Representa: 1x² + 2x + 1

print(f"P1:            {p1}")
print(f"P2:            {p2}")
print(f"Grado P1:      {p1.get_grado()}")
print(f"Coef. líder:   {p1.get_coeficiente_lider()}")
print(f"Términos P1:   {p1.get_terminos()}")

print("-" * 40)

print(f"P1 + P2:       {p1.sumar(p2)}")
print(f"P1 - P2:       {p1.restar(p2)}")
print(f"P1 * P2:       {p1.multiplicar(p2)}")
print(f"P1 evaluado en x=2:  {p1.evaluar(2)}")
print(f"Derivada P1:   {p1.derivar()}")

print("-" * 40)

cociente, residuo = p1.dividir(p2)
print(f"P1 / P2:")
print(f"  Cociente:    {cociente}")
print(f"  Residuo:     {residuo}")