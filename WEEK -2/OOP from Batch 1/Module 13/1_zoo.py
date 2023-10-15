# Its about Abstract Class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @property
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def move(self):
        print("Moving around in the zoo")


class Monkey(Animal):
    def __init__(self):
        self.__name = 'monkey'
    def sing(self):
        print("Monkey is singing")
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def eat(self):
        print("Eating banana")

    def move(self):
        print("Hanging on the branches of the tree")
        super().move()


class Tiger(Animal):
    def eat(self):
        pass
    def move(self):
        pass






monkey1 = Monkey()
print(monkey1)
# monkey1.eat()
# monkey1.move()
monkey1.name = 'moonkey'
print(monkey1.name)





# tiger1 = Tiger()
# tiger1.eat()