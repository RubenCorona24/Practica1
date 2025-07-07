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
print("***WEOLCOME TO THE GAME: Rock, paper, scissors")
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

from datetime import *
#todo esto es un ejercicio de prueba, con el fin de mejorar los conocimientos de poo
#características: jugadores,funciones, entre otras

def pedir_nombre():
    name = input("Hello, what is your name?: ")
    return name


name = pedir_nombre()
age = int(input("Enter your ages: "))


class Jugador:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Tu te llamas {self.name}, tienes {self.age} años"

    def jugando(self):
        print(f"Jugador {self.name} está jugando")


jugador1 = Jugador(name, age)


def inicio():
    try:
        print("Welcome to this tematic of Python")
        print(jugador1)
        if jugador1.age >= 18:
            print("You are a man")
            eleccion = input("What would you like to drink? (beef/wine): ")
            if eleccion not in ['beef','wine']:
                print("That isn't available here")
            else:
                print(f"Good, your have chosen {eleccion}")

        else:
            print("You are a child yet, you can´t have any drink")
    except:
        print("something has gone wrong")

    finally:
        print(f"Thanks for your choice {jugador1.name}")


inicio()


    



