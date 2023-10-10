# Remember:
'''

Instance attributes can't accessed by the name of the class
Instance attributes can be accessed by the object of the class
Class attributes can be accessed by the object and the name of
the class.

'''

soft_eng1 = ["Software Engineer", 'Nayeem', 25, 'Junior', 4000]
soft_des2 = ["Software Designer", 'Sajjad', 25, 'Senior', 9000]


def simple_funciton(parameter):
    print(f'{parameter[1]} is writing a song')


# print()
# simple_funciton(soft_eng1)
# simple_funciton(soft_des2)
# print()


class SoftwareEngineer:
    class_attribute = "I am class attribute"

    def __init__(self, name, age, level, salary):
        # These are instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    def information(self):
        return f"name = {self.name} , age = {self.age}, level = {self.level}"

    def __str__(self):
        return f"name = {self.name}, age = {self.age}, level = {self.level}"

    def __eq__(self, other):
        return self.name == other.name or self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 8000
        return 9000

    @staticmethod
    def hello_func():
        print("Hello Class")


se1 = SoftwareEngineer("Maxwell", 23, "Junior", 5000)
se2 = SoftwareEngineer("Alex", 33, "Senior", 8000)
se3 = SoftwareEngineer("Alex", 34, "Senior", 8000)

# print(se1)
# print(se2)
# print(se3)

# print(se2==se3)
# print(se1.entry_salary(30))

print(se1.entry_salary(22))

print(SoftwareEngineer.entry_salary(33))
SoftwareEngineer.hello_func()

# se1.code()
# se2.code()

# se1.code_in_language('JavaScript')
# se2.code_in_language("Python")


# print(se1.information())
# print(se2.information())


# print(se1.name, se1.age, se1.level, se1.salary)
#
# print(se1.class_attribute)
# print(SoftwareEngineer.class_attribute)
# # print(SoftwareEngineer.name)
# print()
#
