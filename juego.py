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



#Estos son algunas notas para las modificaciones para un mejor entendimiento del juego

class Jugador:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def correr(self):
        print(f"Jugador {self.name} corriendo")
    def comer(self):
        print("El jugador está comiendo")
    def __str__(self):
        return f"Este es un juador llamado {self.name}, tiene {self.age} años y está adentrándose en un bosque profundo y peligroso."

class Depredador:
    def __init__(self,name,habilidad,vida):
        self.name = name
        self.habilidad = habilidad
        self.vida = vida
    def cazar(self):
        print("El depredador esta cazando")
    def atraer(self):
        print("El depredador está atrayendo a la víctima")
    def __str__(self):
        return f"Este depredador llamado {self.name} busca víctimas entre el bosque, tiene la mortal habilidad de {self.habilidad}."

Jugador1 = Jugador('Andy',18)
depredador = Depredador('Lobo','Garras filosas',180)
print(Jugador1)
print(depredador)
#Este es un nuevo comentario desde GitHub
#Ahora tambiene es este otro cambio

lugares = ['bosque','lago','oceano','casa','barco','aereopuerto']
mapa = choice(lugares)
historia = f'erase una vez un niño llamado {Jugador1} que se encontraba en un/a {mapa} abandonado'
class Narrador:
    def narrar(self):
        return historia
    
narrador1 = Narrador()

print(narrador1.narrar())