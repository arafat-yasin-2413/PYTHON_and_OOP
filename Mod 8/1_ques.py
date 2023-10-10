'''
Make a class named Star_Cinema which will have one class attribute
named hall_list which is an empty list initially. Make a method named
entry_hall() to insert an object of class Hall (Described below) inside
its hall_list.
'''


class Star_Cinema:
    __hall_list = []

    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)


class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no):
        super().__init__()
        self.hall_list.append(self)
        self.entry_hall(self)


object1 = Hall(5, 3, 2)
# ei object ta k insert korte hobe
