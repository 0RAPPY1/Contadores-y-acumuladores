cuantas = int(input("¿Cuantos eventos hay? "))
contador = 0
G = 0 # Gryffindor
S = 0 # Slytherin
while contador < cuantas:
  contador += 1
  evento =  input("Coloca el evento (1.goal/2.snitch/3.foul): ").lower()
  
  if evento == "1":
    dequien = input ("¿De quien fue el goal ( 1)Gryffindor / 2)Slytherin )?").lower()
    if dequien == "1":
      G += 10
    if dequien == "2":
      S += 10
 
  elif evento == "2":
    Snithch = input("¿De quien es el snitch ( 1)Gryffindor / 2)Slytherin )?").lower()
    if Snithch == "1":
      G += 150
    elif Snithch == "2":
      S += 150

  elif evento == "3":
    falta = input("¿De quien es el foul ( 1)Gryffindor / 2)Slytherin )?").lower()
    if falta == "1":
      G -= 30
    if falta == "2":
      S -= 30
  else:
    print("Debes de colocar uno")
  
  
print(" ")  
print("Puntos de cada uno:")
print("Gryffindor:", G)
print("Slytherin:", S)
print(" ")

if G > S:
  print("¡Gryffindor gana!")
elif S > G:
  print("¡Slytherin gana!")
else:
  print("¡Es un empate!")
