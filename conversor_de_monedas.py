import os
os.system("cls")

USD = 1
ARS = 290
COP = 4600
MXL = 20

def conversor(moneda):
    dolares = int(input("Cuantos dolares tenes?"))
    pesos = dolares * moneda
    print(f"Tienes {pesos} pesos")


print(f"Bienvenido al conversor de monedas definitivo!")
print(f"Elije una de las siguientes opciones: ")
print("1 - Dólares a pesos argentinos")
print("2 - Dólares a pesos colombianos")
print("3 - Dólares a pesos mexicanos")
opcion = int(input("Cual es la opcion?"))
print("")
#opcion = int(opcion)

if opcion == 1:
    conversor(ARS)
elif opcion ==2:
    conversor(COP)
elif opcion == 3:
    conversor(MXL)
else:
    print("Escribe una opcion correcta")
