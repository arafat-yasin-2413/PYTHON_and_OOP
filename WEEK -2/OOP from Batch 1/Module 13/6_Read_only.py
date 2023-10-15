class Student:
    def __init__(self,name,roll,marks):
        self._name = name
        self.__roll = roll
        self.marks = marks


    # getter, setter
    @property
    def student_id(self):
        return self.__roll

    @property
    def name(self):
        return self._name

    # @name.deleter
    # def name(self):
    #     del self._name




rakib = Student("Rakib",15,65)

# rakib.student_id = 23
# print(rakib.student_id )

print(rakib.name)
# del rakib.name
print(dir(rakib))
print(rakib._name)