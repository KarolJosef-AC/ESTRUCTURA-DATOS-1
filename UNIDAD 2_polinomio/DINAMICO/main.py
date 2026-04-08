from operaciones import polinomio

p1 = polinomio()
p1.agregar_termino(1, 3)   # 1x³
p1.agregar_termino(2, 2)   # 2x²
p1.agregar_termino(3, 0)   # 3

p2 = polinomio()
p2.agregar_termino(1, 2)   # 1x²
p2.agregar_termino(2, 1)   # 2x
p2.agregar_termino(1, 0)   # 1

print(f"P1:            {p1}")
print(f"P2:            {p2}")
print(f"Grado P1:      {p1.get_grado()}")
print(f"Cabeza P1:     coef={p1.get_cabeza().coeficiente}, exp={p1.get_cabeza().exponente}")
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
print("P1 / P2:")
print(f"  Cociente:    {cociente}")
print(f"  Residuo:     {residuo}")