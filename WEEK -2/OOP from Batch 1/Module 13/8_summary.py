# abstract class

class Book:
    def __init__(self,name):
        self.name = name


    def read(self):
        raise NotImplementedError

    def exercise(self):
        pass

class Physics(Book):
    def __init__(self,name):
        super().__init__(name)

    def read(self):
        print("Reading this book")



topon = Physics("Physics HSC")
# topon.read()
topon.exercise()