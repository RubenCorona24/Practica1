def clasificar_num(num):
    if num %2 == 0:
        return f"{num} es par"
    else:
        return f"{num} es impar"
    
print(clasificar_num(5))

def clasificar_numeros(*args):
    pares = []
    impares = []
    for arg in args:
        if arg %2 == 0:
            pares.append(arg)
        else:
            impares.append(arg)
    return f"Estos números son pares: {pares}"

        
print(clasificar_numeros(8,4,8,9,24,7,86,6))

def describir_modelo(modelo,**kwargs):
    print(f"El modelo es {modelo}")
    for atributo,valor in kwargs.items():
        print(F"{atributo}:{valor}")

describir_modelo("Toledo 2017",color="rojo",precio="1200mxm",fábrica="Taiwan")

from random import choice
def sorteo(*args):
    return choice(args)
print(sorteo(1,2,3))

r = 'si'
while r == 'si':
    r = input("Quieres seguir?")
else:
    print("Gracias")
   

def convertir_cuadrado(num):
    return num**2
print(convertir_cuadrado(2))

def num_cuadrados(*args):
      return [(arg**2) for arg in args]

print(num_cuadrados(1,2,3))
from random import *

#Función de escoger un número, personaje y lugar
personajes = ['Adolfo','Raul','Alonso']
num = randint(1,101)
lugar = choice(['laberinto','plaza','bosque'])
print(F"Te toco personaje: {choice(personajes)} número: {num} lugar: {lugar}}")
        
                   
   