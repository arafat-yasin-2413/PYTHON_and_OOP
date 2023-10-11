
class Student:

    def __init__(self,name,cls,fee):
        self.name = name
        self.cls = cls
        self.fee = fee


    def __repr__(self):
        return f"Student with name {self.name} , class : {self.cls}, fee : {self.fee}"


class Teacher:
    def __init__(self,t_name,t_subject,t_id):
        self.name = t_name
        self.subject = t_subject
        self.id = t_id

    def __repr__(self):
        return f"Teacher's name : {self.name}, Subject : {self.subject}, ID : {self.id}"

class School:
    def __init__(self, name):
        self.school_name = name
        self.students = []
        self.teachers = []
        self.min_fee = 6500

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll_student(self,name,cls,fee):
        if fee < self.min_fee:
            return 'Fee is not enough'
        else:
            id = len(self.students) + 1
            student = Student(name,cls,fee)
            self.students.append(student)


    def __repr__(self):
        print(f"Welcome to {self.school_name}")
        print(f'---------OUR TEACHERS--------')
        for things in self.teachers:
            print(things)

        print()
        print(f'--------OUR STUDENTS---------')
        for things in self.students:
            print(things)
        return 'All done'

# akash = Student("Akash",8,1)
# bokul = Student("Bokul",9,2)
# sadek = Student("Sadek",9,3)
#
# print(akash.name , akash.cls, akash.id)
# print(bokul.name , bokul.cls, bokul.id)
# print(sadek.name , sadek.cls, sadek.id)


phitron = School("Phitron Programming")
phitron.enroll_student("Dalim",11,7000)
phitron.enroll_student("Feluda",10,6600)
phitron.enroll_student("Giant",8,6700)

phitron.add_teacher("Rahat Khan","DSA")
phitron.add_teacher("Firoz Khan","C++")
phitron.add_teacher("Pritom Kundu","SQL")

print(phitron)
