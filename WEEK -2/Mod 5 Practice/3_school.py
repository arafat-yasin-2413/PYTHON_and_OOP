class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        print (f"Student with name : {self.name}, age : {self.age}")


class Student(Person):
    def __init__(self,name,age,st_id):
        super().__init__(name,age)
        self.id = st_id

    def __repr__(self):
        print(f"Student : {self.name}, age : {self.age}, st_id: {self.id}")



class Teacher(Person):
    def __init__(self,name,age,t_id):
        super().__init__(name,age)
        self.id = t_id

    def __repr__(self):
        print(f"Teacher : {self.name}, age: {self.age}, t_id: {self.id}")



class School:
    def __init__(self,name):
        self.name = name
        self.studentsList = []
        self.teachersList = []

    def add_student(self,student):
        self.studentsList.append(student)

    def add_teacher(self,teacher):
        self.teachersList.append(teacher)

    def showTeachers(self):
        print(f"Our Teachers:")
        for teacher in self.teachersList:
            print(teacher)

    def showStudents(self):
        print(f"Our Students:")
        for student in self.studentsList:
            print(student)


student1 = Student("Rakib",16,103)
student2 = Student("Sakib",17,104)

teacher1 = Teacher("Asad Khan",42,1005)
teacher2 = Teacher("Mehedi Sir",36,1006)

my_school = School("William Carrey Int. School")
my_school.add_student(student1)
my_school.add_student(student2)
my_school.add_teacher(teacher1)
my_school.add_teacher(teacher2)

my_school.showTeachers()
my_school.showStudents()
