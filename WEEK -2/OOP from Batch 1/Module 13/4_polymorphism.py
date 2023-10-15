# Polymorphism
# Different vabe kono kaj kora
# situation onushare bivinno roop

class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print("Animal making some sound")


class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_sound(self):
        print('meow meow')



class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

    def make_sound(self):
        # return super().make_sound()
        print('Bark bark')

class Horse(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_sound(self):
        print('neigh neigh')






tuntunibilai = Cat('Tuntuni Bilai')
tuntunibilai.make_sound()

tom = Dog('Tom')
tom.make_sound()

horse1 = Horse('Anton')
horse1.make_sound()


tom2 = Dog('Boro Tom')
tom2.make_sound()


print()
animals = [tuntunibilai,tom,horse1,tom2]

for animal in animals:
    animal.make_sound()
