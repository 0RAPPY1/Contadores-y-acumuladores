'''
Crea un programa que registre los clientes que entran a una tienda y cuántos de ellos
compran varitas. Debe registrar qué clientes compraron qué varitas. Las opciones de varitas
son: 1. Varita de Saúco, 2. Varita de Espino, 3. Varita de Sauce y 4. Varita de Acebo.
'''


CTOTALES = 0 #Clientes totales
CSI = 0 #Clientes que compraron
CNO = 0 #Clientes que no compraron
VVendidas = {"Varita de Saúco": 0, "Varita de Espino": 0, "Varita de Sauce": 0, "Varita de Acebo": 0} #Varitas vendidas

while True:
    print(" ")
    Entra = input("¿Entrar un cliente? (Si/No): ").lower()

    if Entra != 'si':
        break

    CTOTALES+= 1

    comprar_algo = input("¿Compró algo? (Si/No): ").lower()

    if comprar_algo == "si":
        CSI += 1
        print(" ")
        print("Existen las siguientes varitas:")
        print(" ")
        print("1) Varita de Saúco")
        print("2) Varita de Espino")
        print("3) Varita de Sauce")
        print("4) Varita de Acebo ")
        varita_comprada = input("¿Qué varita compró? Elige(1, 2, 3 o 4) : ")

        if varita_comprada in ['1', '2', '3', '4']:
            varita_elegida = {
                '1': 'Varita de Saúco',
                '2': 'Varita de Espino',
                '3': 'Varita de Sauce',
                '4': 'Varita de Acebo'
            }[varita_comprada]

            VVendidas[varita_elegida] += 1
        else:
            print("Opción no válida. No se registrará la compra de varita.")
    else:
      CNO += 1

# Mostrar resultados
print(" ")
print(f"Clientes totales: {CTOTALES}")
print(f"Clientes que compraron: {CSI}")
print(f"Clientes que no compraron: {CNO}")
print(" ")
print(f"Hoy se vendierón") 
print("-----------------")
print(f"{VVendidas['Varita de Saúco']} varitas de sauco")
print(f"{VVendidas['Varita de Espino']} varitas de espino")
print(f"{VVendidas['Varita de Sauce']} varitas de sauce")
print(f"{VVendidas['Varita de Acebo']} varitas de acebo")
print("-----------------")
print("¡Qué gran día para Ollivanders!")
