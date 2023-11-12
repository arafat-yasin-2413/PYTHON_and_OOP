class Book:
    def __init__(self,id,name,quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.password = password

        self.borrowed_books = []
        self.returned_books = []

class Library:
    def __init__(self,name):
        self.name = name

        self.users = []
        self.books = []


    def add_book(self,id,name,quantity):
        for book in self.books:
            if book.id == id:
                print(f"This book with id : {book.id} already exists")
                return
        book = Book(id,name,quantity)
        self.books.append(book)


    def add_user(self,id,name,password):
        pass

    def borrow_book(self,user,token):
        pass

    def return_book(self,user,token):
        pass
