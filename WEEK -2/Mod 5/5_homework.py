import random

class Exam:
    def __init__(self,subject):
        self.subject = subject



    def attended_to_exam(self):
        print(f'Attended to {self.subject}')

    def get_marks(self):
        print(f'Obtained {random.randint(70,80)} in {self.subject}')


sabit = Exam('Bangla')
sabit.get_marks()
sabit = Exam('English')
sabit.get_marks()
sabit = Exam('Math')
sabit.get_marks()


