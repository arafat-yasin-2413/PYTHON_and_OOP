class Student:
    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll


class Course:
    def __init__(self,name,assigned_teacher):
        self.name = name
        self.assigned_teacher = assigned_teacher


class Teacher:
    def __init__(self,t_name,course_niben):
        self.t_name = t_name
        self.course_niben = course_niben

    

class School:
    def __init__(self,name,teachers,courses,students):
        self.name = name
        self.teachers = teachers
        self.students = students

    def get_students(self):
        for student in self.students:
            print(student.name)






ds = Course("Data Structures","Pritom Sir")
teacher1 = Teacher("Pritom Sir",ds)

algo = Course("Algorithm","Farhan Sir")
teacher2 = Teacher("Farhan Sir",algo)


student1 = Student("Alamin",19,54)
student2 = Student("Ashiq",18,65)
student3 = Student("Shamim",19,56)

teacher_list = [teacher1,teacher2]
student_list = [student1,student2,student3]
course_list  = [ds,algo]

my_school = School("Phitron High School",teacher_list,course_list,student_list)

print(my_school.name)
my_school.get_students()
# print(my_school.teachers)

print(type(student2))



