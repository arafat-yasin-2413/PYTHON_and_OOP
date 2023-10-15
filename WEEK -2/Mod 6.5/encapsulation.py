class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age



person1 = Person("Robert",23)
person1.name = "Alex"
print(person1.name)
person1.set_age(34)
print(person1.get_age())