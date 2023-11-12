'''
Desarrolla un programa que calcule el porcentaje de error de un sensor de temperatura
LM35 en un laboratorio. El programa debe detectar y almacenar las lecturas incorrectas,
mostrando al final el porcentaje de veces que el sensor dio valores fuera del rango esperado
(entre 10 y 40 grados Celsius).
'''

contador = 0 
lecturas = int(input("¿Cuantas lecturas tienes? "))

Lcorrectas = 0
Lincorrectas = 0

while contador < lecturas:
  contador += 1
  Itemp = int(input(f"Inserta la temperatura {contador}: "))
  if 10 <= Itemp <= 40:
    Lcorrectas += 1
  else:
    Lincorrectas += 1

porcentaje = (Lincorrectas/(Lcorrectas+Lincorrectas))*100

print(" ")
print(f"Lecturas correctas: {Lcorrectas} ")
print(f"Lecturas incorrectas: {Lincorrectas} ")
print(" ")
print(f"Porcentaje de error {porcentaje}%")
