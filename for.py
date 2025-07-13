print("Hola este es un cajero")
#Variable nombre
nombre = input("Cual es tu nombre?")
ahorro = int(input("cual es tu ahorro?"))
print("muy bien " + nombre + " ¿que opreación deseas hacer? tu saldo es de ", ahorro, "mxn")
#Opciones
ejecutar = True

while ejecutar:
    print( " **** selecciona una opcion **** ")
    print(nombre + " presiona 1 para consultar tu saldo")
    print(nombre + " presiona 2 para hacer un retiro")
    print(nombre + " presiona 3 para hacer un abono")
    print("")
    opcion = int(input("escribe la opcion que deseas usar: "))
    #opción 1 consultar tu saldo

    if opcion == 1:
        print("Tu saldo es de ",ahorro,"mxm")
        opcion_uno= input("Deseas hacer otra operación? ")
        if opcion_uno== "si":
            print("tendrás que regresar al menu principal")
        elif opcion_uno == "no":
            print("Gracias po visitarnos, hasta luego")
            ejecutar = False
        else:
            print("Opción no válida")
    # Opción 2 Retirar

    elif opcion == 2:
        print ("Elegiste la opción de retirar")
        retiro = float(input("Introduce la cantidad que desees retirar: "))
        total = ahorro - retiro
        print(f"Bien {nombre}, retiraste {retiro}mxm y ahora tu saldo es de {total}")
        opcion_dos = input("Quieres continuar? (si_/no): ")
        if opcion_dos == "si":
            print("Tendras que regresar al menú principal")
            ejecutar = True
        elif opcion_dos == "no":
            print("Gracias por visitarnos.")
            ejecutar= False
    
    #Opción 3 hacer abono
    elif opcion == 3:
        print("Elegiste la opción de hacer un abono")
        opcion_tres = int(input("escribe la cantidad que deseas abonar: "))
        resultado = ahorro + opcion_tres    
        print(f"{nombre}, tu saldo ahora es de  {resultado}")

from abc import ABC, abstractmethod


class Object(ABC):
    @abstractmethod
    def moverse(self):
        pass

    @abstractmethod
    def prender_luz(self):
        pass

    @abstractmethod
    def pararse(self):
        pass


class Nissan(Object):
    def __init__(self, año, velocidad):
        self.año = año
        self.velocidad = velocidad

    def moverse(self):
        print(f"El Nissan se mueve a unos {self.velocidad}km por hora")
        nuevo_mov = int(input("Velocidad aumentada: "))
        new_v = self.velocidad + nuevo_mov
        print(f"Ahora se mueve a {new_v}km/hora")

    def prender_luz(self):
        print("Luces prendidas de Nissan")

    def pararse(self):
        self.velocidad = 0
        print(f"Nissan en reposo con {self.velocidad}km por hora")

    def __str__(self):
        return f"Automovil Nissan del año {self.año}, va a una velocidad de {self.velocidad}km/hora"


carro = Nissan(2009, 14)
print(carro)
carro.pararse()
carro.moverse()
carro2 = Nissan(2009,29)
print(carro2)
from random import *

num = randint(1,100)
if num%2 == 0:
    print(f"{num} es par")
else:
    print(f"{num} es impar")
from datetime import*
class Caricatura:
    def __init__(self,titulo,año,creador):
        self.año = año
        self.creador = creador
        self.titulo = titulo

    def presentar(self):
        return f"La caricatura {self.titulo} fue creada por {self.creador} en el año {self.año}"
class Trabajo:
    def __init__(self,empresa,posición):
        self.empresa =empresa
        self.posicion = posición
    def presentar(self):
        return f"Trabajas en una insitusión llamada {self.empresa} como {self.posicion}"
try:
    edad = int(input("Selecciona tu edad: "))
    if edad in range(1,12):
        print("Eres un niño todavía")
        caritcatura = input("Cuál es la caricatura que más ves?: ")
        fecha = input(f"Recuerdas en que fecha se estrenó {caritcatura}?(si/no): ")
        if fecha == 'si':
            date = int(input("Vale, introduce la fecha de estreno: "))
        elif fecha == 'no':
            print("No te preocupes, le asignamos una fecha")
            year = randint(1900,2025)
            month = randint(1,13)
            day = randint(1,31)
            date = date(year,month,day)
            print(f"La fecha de estreno fue: {date}")
        else:
            year = randint(1900,2025)
            month = randint(1,13)
            day = randint(1,31)
            date = date(year,month,day)
            print(f"No introduciste una respuesta clara, pero le asignamos una fecha:{date} vale ")
        autor = input("Quien fue el autor de tu caricatura?: ")
        caricatura = Caricatura(caritcatura,date,autor)
        print(F"Vale, tenemos los datos de tu caricatura: {caricatura.presentar()}")



    elif edad in range(12,18):
        print("Eres un adolescente")
        videojuego = input("Tienes algún videojuego favorito?(no/si): ")
        if videojuego == 'si':
            favorito = input("Vale, cual es tu videojuego favorito?: ")
            print(f"Que bien, tienes buenos gustos al interesarte en {favorito}")
        elif videojuego == 'no':
            print("No pasa nada, a veces uno se divierte más con libros o canciones")
        else:
            print("Mmm no entendí el mensaje, pero está bien supongo jajaja")
    elif edad in range(18,45):
        print("Eres un adulto")
        trabajo = input("En este momento tienes un trabajo establecido?(si/no): ")
        if trabajo == 'si':
            job = input("Genial, como se llama la empresa donde trabahas?: ")
            posiiton = input(f"Cuál es tu puesto en la empresa {job}?: ")
            tu_trabajo = Trabajo(job,posiiton)
            print(F"Vale, te voy a decir tus datos como trabajador: {tu_trabajo.presentar()}")
        elif trabajo == 'no':
            print("No te preocupes, cualquier día es una nueva oportunidad")
    else:
        print("Eres ya un anciano")
        travel = input("Te gustaría viajar en un lugar en especial?(si/no): ")
        if travel =='si':
            lugar = input("Dónde te gustaría viajar?: ")
            print(f"Muy bien, a mi también me gustaría viajar a {lugar}!!")
        elif travel == 'no':
            print("Está bien, a veces es mejor quedarse en casa!!")   

except:
    print("Algo ha salido mal")
finally:
    print("Proceso finalizado, gracias")        
        

