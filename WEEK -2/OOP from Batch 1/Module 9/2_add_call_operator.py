class Person:
    def __init__(self,name,age,money,height = 65):
        self.name = name
        self.age = age
        self.money = money
        self.height = height

    def __call__(self):
        return f"Name = {self.name}, age = {self.age}, money = {self.money}"

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self,other):
        return self.money == other.money

    def __repr__(self):
        return f"Name : {self.name}, age : {self.age}, money : {self.money}"

    # def __str__(self):
    #     return f"Name is : {self.name}, age is : {self.age}, money is : {self.money}"


    def __len__(self):
        return self.height

alim = Person("Alim",23,450,76)
dalim = Person("Dalim",26, 450)

# print(alim())
# print(dalim())

# print(alim > dalim)
# print(alim == dalim)

# print(alim)
# print(dalim)

print(len(alim))


'''
object 'alim' is not callable. to make the object callable we have implemented 
__call__ function. That's the outcome of this video. 

'''