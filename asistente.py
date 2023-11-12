'''
Escribe un programa que detecte si se escribe 'Alexa' en un texto. Si se escribe más de una
vez, el programa debería responder "Tranquilo, solo di mi nombre una vez". Tip: usa las
funciones split() para separar el texto y count() para identificar las veces que dice Alexa.
'''

nombre = input("Coloca tu nombre: ")
while True:
  print(" ")
  llama = input("Llama a Alexa: ").lower().split()
  
  c = llama.count('alexa') #Cuenta las veces que dice Alexa

  if c == 1:
    print(f"¡Hola {nombre}!")
    break
  elif c > 1:
    print(f"Tranqui {nombre} solo di mi nombre una vez")
  else:
    print(f"No dijiste mi nombre {nombre}")
