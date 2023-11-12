from School import School,Classroom
from Persons import Student


def main():
    school = School('Adamjee Cant','Uttara')


    eight = Classroom('Eight')
    school.add_classroom(eight)
    nine = Classroom('Nine')
    school.add_classroom(nine)
    ten = Classroom('Ten')
    school.add_classroom(ten)

    abir = Student('Abir Khan',eight)
    school.student_admission(abir)


    print(school)











if __name__ == '__main__':
    main()
