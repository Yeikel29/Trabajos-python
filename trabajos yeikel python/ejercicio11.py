import random

opciones = ["piedra", "papel", "tijera"]

computadora = random.choice(opciones)

Paper = "papel"
sissors = "tijeras"
stone = "piedra"

opcion = input("Escoja piedra, papel o tijera: ")

if opcion == computadora:
	print("empate")
elif ((opcion == "piedra" and computadora == "tijera") or 
	  (opcion == "papel" and computadora == "piedra") or 
	  (opcion == "tijera" and computadora == "papel")):
	print("ganaste")
else:
	print("perdio")