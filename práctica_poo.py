from abc import ABC, abstractclassmethod

class SerVivo(ABC):
    def __init__(self,age,name,height):
        self.age = age
        self.name = name
        self.height = height
    @abstractclassmethod
    def born(self):
        print("The living being was born")
    @abstractclassmethod
    def breathe(self):
        print("The living being is breathing")

    @abstractclassmethod
    def eat(self):
        print("The living being is eating")

living_being = SerVivo(19,'Juan','170cm')
print(living_being)