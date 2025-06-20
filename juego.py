from random import *
name = input("Dime tu nombre: ")
print(f"Bien jugador, tu nombre es: {name}")
num = randint(1,101)
print(f"jugador {name}, tu número seleccionado es: {num}")
area = ['parque','espacio','vecindario','escuela','hospital','bosque']
area_seleccionada = choice(area)
print(f"Jugador {name},en total se disponen de {len(area)} mapas en nuestro juego, hemos seleccionado tu mapa de juego, te tocó : {area_seleccionada}")
print("***QUE EMPIEZE EL JUEGO***")
print("INSTRUCCIONES \n Debes de completar todas las misiones sin excepción, al finalizar tu recompensa \n se te dara con un total de 100 monedas")


vidas = 3
while vidas:
    pass


