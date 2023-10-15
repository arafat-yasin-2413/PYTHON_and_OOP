class Laptop:

    def __init__(self,brand,age):
        self.brand = brand
        self.age = age

    def increase_age(self,age_2 = 7):
        self.age = self.age + 1 + age_2

    def repair(self,lifetime):
        self.increase_age(lifetime)


my_laptop = Laptop("Macbook", 2)
print(my_laptop.age)
# my_laptop.increase_age(9)
print(my_laptop.age)
# my_laptop.repair(-5)
print(my_laptop.age)
print(my_laptop.__dict__)  # ekta class er moddhe ki ki attribute niyechi seta dekhar jonno ei function ta use kora hoy.

