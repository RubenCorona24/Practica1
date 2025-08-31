#Vamos a programar orientado a objetos
from abc import ABC,abstractmethod

class Humano(ABC):
    def __init__(self,edad,name,altura):
        self.edad = edad
        self.name = name
        self.altura = altura
    @abstractmethod
    def presentarse(self):
        pass
    @abstractmethod
    def respirar(self):
        pass
    @abstractmethod
    def comer(self):
        pass

class Estudiante(Humano):
    def __init__(self, edad, name, altura, grado, escuela):
        super().__init__(edad, name, altura)
        self.grado = grado
        self.escuela = escuela

    def presentarse(self):
        return f"Hola, mi nombre es {self.name}, tengo {self.edad} años, voy en la escuela {self.escuela} en el grado {self.grado}"
    
    def respirar(self):
        print(f"{self.name} está respirando")
    def comer(self):
        print(f"{self.name} está comiendo su comida favorita")

class Trabajador(Humano):
    def __init__(self, edad, name, altura,empresa,ocupación):
        super().__init__(edad, name, altura)
        self.empresa = empresa
        self.ocupacion = ocupación
    def presentarse(self):
        return f"Hola mi nombre es {self.name}, tengo {self.edad} años, soy trabajador de la empresa {self.empresa} como {self.ocupacion}"
    def comer(self):
        print(F"{self.name} está comiendo su comida favorita")
    def respirar(self):
        print(F"{self.name} está resírando")
estudiante = Estudiante(19,'Andrés Garza',199,6,'Tecnológico de Monterrey')
trabajador1 = Trabajador(34,'Fernando',168,'RUV','CEO')
ocupantes = [estudiante,trabajador1]
def presentar(ocupantes): #Función de polimorfismo
    for o in ocupantes:
        o.presentarse()
try:
    presentar(ocupantes)
except:
    print("ERROR")


def verificar_estudiante(personaje):
    if personaje.edad >= 18:
        print("Es adulto")
    else:
        print("No es adulto")
verificar_estudiante(trabajador1)

def crear_personaje():
    print("------Bienvenido a la creación de personajes------")
    try:
        name = input("Dime tu nombre: ")
        years = int(input("Dime tu edad: "))
        hight = float(input("Cuánto mides?: "))
    except:
        print(F"Error, ingresaste mal datos")
    estado = input(f"{name}, eres trabajador o estudiante?: ").lower()
    if estado == 'trabajador' or estado == 'trabajo':
        empresa = input("En qué empresa trabajas?: ")
        ocupacion = input(f"Puesto que tienes en la empresa {empresa}: ")
        if name and years and estado and hight and empresa and ocupacion:
            personaje = Trabajador(years,name,hight,empresa,ocupacion)
            with open("archivos_aparte\\personajes.txt",'a') as file:
                file.write(f"---{personaje.presentarse()}\n")
        else:
            print("Error, faltaron datos por llenar")
    elif estado == 'estudiante' or estado=='estudio':
        escuela = input(f"{name}, dime nombre de tu escuela: ")
        grado = int(input(f"Grado que cursas en {escuela}: "))
        if name and years and estado and hight and escuela and grado:
            personaje = Estudiante(years,name,hight,grado,escuela)
            with open("archivos_aparte\\personajes.txt",'a') as file:
                file.write(f"---{personaje.presentarse()}\n")
        else:
            print("Error, faltaron datos por llenar")
    return f"Listo {name}, hemos creado tu ficha de presentación!!\n{personaje.presentarse()}" 
    

def menu():
    while True:
        print("*" *20 + "Bienvenido al menú de personajes" + "*" *20)
        print(f"Tienes 3 opciones en este menú:\n1: Crear personaje\n2: Ver personajes\n3: Salir")
        eleccion = int(input("Qué opción eliges?: "))
        if eleccion == 1:
            print(crear_personaje())
            continue
        elif eleccion == 2:
            with open("archivos_aparte\\personajes.txt",'r') as file:
                print(file.read())
                continue
        elif eleccion == 3:
            print("Muchas gracias por tu atención!!")
            break
        else:
            print(f"Error, solo puede escoger (1,2,3)")
try:
    menu()
except Exception as e:
    print(f"ERROR, {e}")
else:
    print(F"Proceso exitoso")
