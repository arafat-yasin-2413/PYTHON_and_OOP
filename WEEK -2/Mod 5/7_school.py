# class,classroom, teacher,students

class Student:
    def __init__(self,name,cls,id):
        self.name = name
        self.cls = cls
        self.id = id

    def __repr__(self):
        return f'Student with name {self.name}, class : {self.cls} id : {self.id}'



class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"Teacher's name : {self.name}, Subject : {self.subject}, id = {self.id}"



class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll_student(self,name,fee):
        if fee < 6500:
            return 'Fee is not enough'
        else:
            id = len(self.students) + 1
            student = Student(name,8,id)
            self.students.append(student)
            return f'{name} is enrolled with id : {id}, extra money : {fee-6500}'
    def __repr__(self):
        print(f'Welcome to {self.name}')
        print(f'-------OUR Teachers-------')
        for teacher in self.teachers:
            print(teacher)


        print(f'------OUR Students--------')
        for student in self.students:
            print(student)
        return 'All done '


# Alina = Student('Alina',9,1)
# print(Alina.name)
# print(Alina.cls)
# print(Alina.id)
# print(Alina)

# rahat = Teacher('Rahat Khan', 'Data Structures', 3)
# print(rahat)


phitron= School('Phitron')
phitron.enroll_student('Alina',5200)
phitron.enroll_student('Rani',8000)
phitron.enroll_student('Rakib',9000)
phitron.add_teacher('Tom Cruise','DS')
phitron.add_teacher('Mosh Hamedani',"Algorithm")
phitron.add_teacher("Farhan Firoz",'C++')


print(phitron)