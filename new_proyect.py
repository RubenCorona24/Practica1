from random import *
import os
from datetime import *


def open_file():
    file = input("File: ")
    arch = open(file, 'r')
    readable = arch.read()
    print(readable)



print("Welcome to the open file system from Python")
route = os.getcwd()
date = datetime.today()
print(f"Your route is {route}")
try:
    open_file()
except:
    print("FailedNotFound")
else:
    print("Succesfull process")
finally:
    print("End of the Process")

print("***DISEÑADOR DE LETRAS Y NÚMEROS***")
from random import *
try:
    text = input("Select text: ").lower()
    letter = choice(['a','b','c','d','f','g','h','i'])
    if letter in text:
        print(f"There is a letter {letter} in your text")
except:
    print("Failed with the string")


vidas = 5
vidas_contra = 5
def poner_jugada():
    jugada = input("Escoge: (piedra/papel/tijera): ")
    return jugada

def asignar_rival():
    jugada = choice(['piedra','papel','tijera'])
    return jugada

print("Es hora de empezar el juego")
def jugadas(jugada_jugador,jugada_rival):
    global vidas, vidas_contra
    if jugada_jugador== 'piedra' and jugada_rival == 'piedra':
      print("Es un empate")
    elif jugada_jugador == 'piedra' and jugada_rival == 'papel':
        print("Jugador:Piedra Rival: Papel-----Rival gana")
        vidas -=1
    elif jugada_jugador == 'piedra' and jugada_rival == 'tijera':
        print("Jugador: Piedra Rival: Tijera---Jugador gana")
        vidas_contra -=1
    elif jugada_jugador=='papel' and jugada_rival == 'piedra':
        print("Jugador: Papel Rival: Piedra---Jugador gana")
        vidas_contra -=1
    elif jugada_jugador == 'papel' and jugada_rival == 'papel':
        print("Jugador: papel Rival: Papel----Empate")
    elif jugada_jugador =='papel' and jugada_rival =='tijera':
        print("Jugador:Papel Rival:Tijera----Rival gana")
        vidas -=1
    elif jugada_jugador == 'tijera' and jugada_rival == 'piedra':
        print(f"Jugador: Tijera Rival: Piedra----Rival gana")
        vidas -=1
    elif jugada_jugador =='tijera' and jugada_rival == 'papel':
        print("Jugador: Tijera Rival: Papel----Jugador gana")
        vidas_contra -=1
    elif jugada_jugador == 'tijera' and jugada_rival=='tijera':
        print("Jugador: Tijera Rival: Tijera----Empate")

while vidas >  0 and vidas_contra > 0:
    jugada1 = poner_jugada()
    jugada1_rival = asignar_rival()
    resultado = jugadas(jugada1,jugada1_rival)
    if vidas == 0:
        print("----El rival ha ganado-----")
    elif vidas_contra == 0:
        print("---El jugador ha ganado---")



