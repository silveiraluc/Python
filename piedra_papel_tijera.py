import os
os.system("cls")

eleccion = input("Elije tu opción: ")


if eleccion == "Papel" or eleccion == "papel":
    print("Computadora elije tijera, Gana la pompu :)")
elif eleccion == "Piedra" or eleccion ==  "piedra":
     print("Computadora elije papel, Gana la pompu :)")
elif eleccion == "Tijeras" or eleccion ==  "tijeras":
     print("Computadora elije piedra, Gana la pompu :)")
else:
     print("elije una opcion correcta :(")
