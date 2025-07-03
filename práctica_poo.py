from abc import ABC, abstractmethod


class SerVivo(ABC):
    def __init__(self, age, name, height):
        self.age = age
        self.name = name
        self.height = height

    @abstractmethod
    def born(self):
        pass

    @abstractmethod
    def breathe(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def __str__(self):
        return f"Age: {self.age} Name: {self.name} Height: {self.height}"


class Human(SerVivo):
    def __init__(self, age, name, height):
        super().__init__(age, name, height)

    def born(self):
        print("The human was born")

    def breathe(self):
        print("The human is breathing")

    def eat(self):
        print("The human is eating")

    def presentarse(self):
        print(f"Hello my name is {self.name}, and I'm {self.age} years old")

human1 = Human(14, 'Sam', '160cm')
human1.presentarse()
print(human1)

human2 = Human(21,'Ralff','175cm')
human2.presentarse()

def comprobar_edad(edad):
    if edad <18:
        print(f"Is younger, has {edad} years old")
    elif edad >= 18:
        print(f"Is an adult, has {edad} years old")
    elif edad >= 50:
        print(f"Is old, has {edad} years old")

comprobar_edad(human1.age)

comprobar_edad(human2.age)


try:
    new_name = input("Enter a name for a new character: ")
    age = int(input("Years of the new character: "))
    height = input("Height of the new character: ")
    new_character = Human(age,new_name,height)
except:
    print("Something has failed")

else:
    new_character.presentarse()
    print("Succesfull process")
finally:
    print("End of the new character")


import datetime
from random import *
#year = randint(2000,2201)
#month = randint(1,13)
#if month == 2:
 #   day = randint(1,29)
#elif month== 4 or 6 or 9 or 11:
 #   day = randint(1,31)
#else:
 #   day = randint(1,32)


#date = datetime.date(year,month,day)
#print(f"Today is {date}")

import os
#Abrir archivos
route = os.getcwd()
print(f"My route is: {route}")
os.chdir("C:\\Users\\coron\\OneDrive\\Escritorio\\Alternativo")
file = open('otro_archivo.txt','r')
arch = file.read()
try:
    print(arch)
except:
    print("FileNotFound")
finally:
    print("End of the Process")
    





    

