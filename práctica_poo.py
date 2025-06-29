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