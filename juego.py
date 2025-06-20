name = input("Dime tu nombre: ")
print(f"Bien jugador, tu nombre es: {name}")
num = randint(1,101)
print(f"jugador {name}, tu número seleccionado es: {num}")
area = ['parque','espacio','vecindario','escuela','hospital','bosque']
area_seleccionada = choice(area)
print(f"Jugador {name}, hemos seleccionado tu mapa de juego, te tocó : {area_seleccionada}")
print("***QUE EMPIEZE EL JUEGO***")

