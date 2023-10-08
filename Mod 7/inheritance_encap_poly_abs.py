# INHERITANCE and OVERRIDING
'''

# Parent Class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

# Child Class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Bark"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"


dog = Dog("Tom")
cat = Cat("Jerry")

print(dog.speak())


'''












# ENCAPSULATION


# '''
# class Student:
#     def __init__(self,name,roll):
#         self.name = name
#         self.__roll = roll # roll is private now
#
#     def get_roll(self):
#         return self.__roll
#
#     def set_roll(self,roll):
#         self.__roll = roll
#
#     def set_name(self,name):
#         self.name = name
#
#
#
#
# student = Student("Jony Harris",103)
# print(student.name, student.get_roll())
# # student.roll = 104 # public attribute hoile eivabe value change kora jay
# # print(student.name, student.get_roll())
# print(student.get_roll())
# student.set_roll(110)
# print(student.get_roll())
# student.set_name("Enayet")
# print(student.name)
# print(student.name, student.get_roll())
#
#
# '''
#
#
#
#
#
#
#
# # POLYMORPHISM
#
# '''
# class Animal:
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "Bark"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
# def make_speak(animal):
#     print(animal.speak())
#
#
# dog = Dog()
# cat = Cat()
#
# make_speak(dog)
# make_speak(cat)
#
#
# '''







# Abstract Classes and Methods

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius


circle = Circle(5)
print(circle.area())














