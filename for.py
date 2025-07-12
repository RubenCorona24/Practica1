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

class Nissan(object):
    def __init__(self, año, velocidad):
        self.año = año
        self.velocidad = velocidad

    def prender_luz(self):
        print("Luces prendidas de Nissan")

    def pararse(self):
        self.velocidad = 0
        print(f"Nissan en reposo con {self.velocidad} km por hora")

    def moverse(self):
        print(f"El auto Nissan se está moviendo a {self.velocidad} km/h")

    def __str__(self):
        return f"Automóvil Nissan del año {self.año}, va a una velocidad de {self.velocidad} km/hora"

# Código de prueba
carro = Nissan(2009, 14)
print(carro)
carro.pararse()
carro.moverse()

carro2 = Nissan(2009, 29)
print(carro2)



        
        

