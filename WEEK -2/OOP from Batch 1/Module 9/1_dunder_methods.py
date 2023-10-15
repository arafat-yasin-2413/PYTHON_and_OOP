# def add(x,y):
#     return x + y
#
# print(add(5,6))
# print(add("Sohel ","khan").upper())





class Person:
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money

    def __add__(self, other):
        return self.age + other.age


sakib = Person("Sakib Al Hasan",34,400)
rakib = Person("Rakib Chowdhury", 40,700)

# my_dict = sakib.__dict__
# print(my_dict)

print(sakib + rakib)