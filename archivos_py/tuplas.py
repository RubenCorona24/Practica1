print("Una tupla es en parétesis")
auto = ("Nissan",2009,'4','1800km')
(marca,año,puertas,velocidad) = auto
def presentar(marca,año,puertas,velocidad):
        print(f"La marca del auto es u: {marca}\nEl año de la marca es de : {año}\nNo. de puertas del auto : {puertas}\nVelocidad del auto {marca}: {velocidad}")
presentar(marca,año,puertas,velocidad)

class Auto:
        def __init__(self,modelo,anio,velocidad,gasolina):
                self.modelo = modelo
                self.anio = anio
                self.velocidad = velocidad
                self.gasolina = gasolina
        def presentar_auto(self):
                return f"Auto modelo {self.modelo}, del año {self.anio}, con una velocidad de {self.velocidad}km/hora"
        def poner_gasolina(self):
                cantidad = int(input("Cantidad de gasolina agregada: "))
                self.gasolina =int(self.gasolina) + cantidad
                print(f"Bien, ahora tienes {self.gasolina} de gasolina")
        def manejar_auto(self):
                if int(self.gasolina) <= 0:
                        print(f"Error, no hay suficiente gasolina")
                        return Auto.poner_gasolina(self)
                        
                

                else:      
                        tiempo = int(input("Tiempo de manejo: "))
                        gasolina_gastada = tiempo*0.5
                        self.gasolina = int(self.gasolina) - gasolina_gastada
                        return f"Ahora cuentas con {self.gasolina} de gasolina"
        

mi_auto = Auto('Toledo',2009,'1200','124')
print(f"Actualmente tu auto {mi_auto.modelo} tiene {mi_auto.gasolina} de gasolina")
print(mi_auto.manejar_auto())
print(mi_auto.manejar_auto())
print(mi_auto.manejar_auto())
print(mi_auto.manejar_auto())
print(mi_auto.manejar_auto())