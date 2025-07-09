#Creamos la clase Persona con atributos nombre y edad
class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def saludar(self):
        print("Hola como están?")

persona = Persona('Rubén',16)

class Cuenta:
    def __init__(self,titular,saldo):
        self.titular= titular
        self.saldo = saldo

    def depositar(self):
        cantidad = int(input("Elige la cantidad a depositar: "))
        new_saldo =self.saldo+cantidad
        print(f"Tu nuevo saldo es de: {new_saldo}mxm")

    def retirar(self):
        cantidad = int(input("Elige la cantidad a retitar: "))
        new_saldo =self.saldo-cantidad
        print(f"Tu nuevo saldo es de: {new_saldo}mxm")
    
    def mostrar_saldo(self):
        print(f"Hola, tu saldo es de : {self.saldo}mxm")
    
    def __str__(self):
        return f"Hola, tu titular es de {self.titular} y cuentas con {self.saldo}mxm"

mi_cuenta = Cuenta('BBVA',1900)
print(mi_cuenta)
mi_cuenta.depositar()

persona2 = Persona('Julio',19)
def mostrar_persona_cuenta(persona,cuenta,saldo):
    print(f"El nombre de la persona es {persona}, su cuenta es de {cuenta} y tiene {saldo}mxm")

mostrar_persona_cuenta(persona2.name,mi_cuenta.titular,mi_cuenta.saldo)

#Clase base
class Empleado:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def trabajar(self):
        print(f"{self.name} está trabajando")
        
    def mostrar_info(self):
        return f"La persona se llama {self.name}, tiene un salario de {self.salary}mxm mensuales"
    def cobrar(self):
        print(f"El trabajador {self.name} cobra {self.salary}mxm")
class Gerente(Empleado):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def mostrar_info(self):
        return f"La persona se llama {self.name}, gana {self.salary}mxm mensuales como gerente y está en el departamento de {self.department}"
    
empleado1 = Empleado('Ricardo',1900)
gerente = Gerente('Francisco',2900,'Ciencias Sociales')
print(empleado1.mostrar_info())
print(gerente.mostrar_info())

empleado2 = Empleado('Jonathan',1830)
empleado3 = Empleado('Kenneth',1730)
empleado3.cobrar()
gerente.cobrar()

