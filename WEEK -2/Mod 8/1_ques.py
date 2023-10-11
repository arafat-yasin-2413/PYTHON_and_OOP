'''
Make a class named Star_Cinema which will have one class attribute
named hall_list which is an empty list initially. Make a method named
entry_hall() to insert an object of class Hall (Described below) inside
its hall_list.
'''

class Hall:
    def __init__(self,row,col,hall_no):
        self.row = row
        self.col = col
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []



class  Star_Cinema:
    __hall_list = []

    def __init__(self,row,col,hall_no):
        super().__init__(row,col,hall_no)
        Star_Cinema.__hall_list.append(self)

    def entry_hall(self):
        pass



Star_Cinema.entry_hall("")