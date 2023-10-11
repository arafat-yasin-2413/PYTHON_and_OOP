# Overriding and Overloading

class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print(f'Vat , meat, polau')

    def exercise(self):
        raise NotImplementedError



class Cricketer(Person):
    def __init__(self,name, age, height,weight,team):
        self.team = team
        super().__init__(name,age,height,weight)

    def eat(self):
        print('Vegetables')

    def exercise(self):
        print('Exercise kori, sustho thaki')

    def __add__(self,other):
        return self.age + other.age
        # return self.height + other.height

sakib = Cricketer("Sakib",38,68,83,'BD')
# sakib.eat()
# sakib.exercise()

mushfiq = Cricketer("Mushfiq",36,65,78,'BD')


print(sakib + mushfiq)
