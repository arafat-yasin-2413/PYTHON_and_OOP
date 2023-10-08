class User:
    def __init__(self,name,age,money):
        self._name = name
        self._age = age
        self.__money = money
    @property
    def age(self):
        return self._age

    @property
    def salary(self):
        return self.__money

    # setter
    @salary.setter
    def salary(self,value):
        if value < 0:
            print('Salary can not be negative')
        self.__money += value






sami = User("Sami Rahman",21,12000)
# print(sami._name)
# print(sami._age)
# print(sami.__money)

# print(sami.get_age())
print(sami.age)
print(sami.salary)

sami.salary = 3000
print(sami.salary)



