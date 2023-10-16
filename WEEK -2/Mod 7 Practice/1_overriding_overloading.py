class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Burger, Pizza, Sandwich")

    def exercise(self):
        # raise NotImplementedError
        print('Person is exercising')
class Cricketer(Person):
    def __init__(self,name,age,height,weight,team):
        self.team = team
        super().__init__(name,age,height,weight)

    def eat(self):
        print("Cricketer is eating healthy food")

    def __add__(self, other):
        return self.age + other.age

    def __gt__(self, other):
        return self.age > other.age

    def __len__(self):
        return self.height

    # def exercise(self):
    #     print('Cricketer is exercising')

sakib = Cricketer("Sakib",36,67,85,'BD')
rakib = Cricketer("Rakib",34,66,78,'BD')
# sakib.eat()
# sakib.exercise()

# print(sakib+rakib)
# print(sakib > rakib)
print(len(sakib))





''' 
def __add__
def __mul__
def __gt__
def __len__

'''