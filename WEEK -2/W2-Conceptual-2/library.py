# class Book:
#     def __init__(self,id,name,quantity):
#         self.id = id
#         self.name = name
#         self.quantity = quantity
#
#
#
#
# class User:
#     def __init__(self,id,name,password):
#         self.id = id
#         self.name = name
#         self.password = password
#         self.borrowed_books = []
#         self.returned_books = []
#
#     def __repr__(self):
#         return f"User name : {self.name} with id : {self.id}"
#
# class Library:
#     def __init__(self,name):
#         self.name = name
#         self.books = []
#         self.users = []
#
#     def add_book(self,id,name,quantity):
#         for book in self.books:
#             if book.id == id:
#                 print(f"Book with {book.id} already exists")
#                 return
#         book = Book(id,name,quantity)
#         self.books.append(book)
#         print(f"Book with name {book.name} {quantity} pcs. added successfully")
#
#
#     def add_user(self,id,name,password):
#         for user in self.users:
#             if user.id == id:
#                 print(f'User id {user.id} already exists')
#                 return
#         user = User(id,name,password)
#         self.users.append(user)
#         return user
#
#
#
#     def borrow_books(self,user,token):
#         for book in self.books:
#             if book.id == token:
#                 if book in user.borrowed_books:
#                     print(f"You have borrowed this book already!")
#                     return
#                 elif book.quantity == 0:
#                     print(f"No copy of this book is available! ")
#                     return
#                 else:
#                     user.borrowed_books.append(book)
#                     book.quantity -= 1
#                     print(f"You have borrowed '{book.name}' successfully. ")
#                     return
#         print(f"Not found any book with id : {token} ! ")
#
#
#     def return_book(self,user,token):
#         for book in self.books:
#             if book.id == token:
#                 if book in user.borrowed_books:
#                     book.quantity +=1
#                     user.borrowed_books.remove(book)
#                     user.returned_books.append(book)
#                     print(f"Returned {book.name} successfully. ")
#                     return
#
#                 else:
#                     print(f"I had not borrowed this book with name {book.name}!!")
#                     return
#
#         print(f'This book is not given to you by us !')
#
#
#
# # main starts from here
#
# library1  = Library("City Library")
#
# admin = library1.add_user('1000',"Admin",'admin1234')
# rakib = library1.add_user(135,'Rakib Hossen','rakib135')
# cpBook = library1.add_book(412,'CP Basic',10)
#
# current_user = admin
# changeOfUser = True
#
# while(True):
#     if current_user == None:
#         print(f"No logged in user found")
#         option = input("Login or Register (L/R) : ").upper()
#         if option == 'L':
#             id = int(input('Enter user id : '))
#             password = input('Enter user password : ')
#
#             ismatch = False
#             for user in library1.users:
#                 if user.id == id and user.password == password:
#                     current_user = user
#                     changeOfUser = True
#                     ismatch = True
#                     break
#
#             if ismatch == False:
#                 print(f"No user found ! ")
#         elif option == 'R':
#             id = int(input('Enter id : '))
#             name = input('Enter your name : ')
#             password = input('Enter password : ')
#
#             for user in library1.users:
#                 if user.id == id:
#                     print(f'This user is already exists. ')
#
#             user = library1.add_user(id,name,password)
#             library1.users.append(user)
#             current_user = user
#             changeOfUser = True
#
#         else:
#             if changeOfUser:
#                 print('----------------------')
#                 print(f"Welcome back {current_user.name}")
#                 print('----------------------')
#                 changeOfUser = False
#             else:
#                 print('-----------------------')
#             if current_user.name == admin:
#                 print('Options: \n')
#                 print("1: Add Book")
#                 print("2: Show Users")
#                 print('3: Show Books')
#                 print('4 : Logout')
#
#                 ch = int(input('Enter your choice'))
#
#                 if ch == 1:
#                     id = int(input('Enter book id : '))
#                     name = input("Enter book's name : ")
#                     quantity = input('Enter book quantity : ')
#
#                     library1.add_book(id,name,quantity)
#
#                 elif ch == 2:
#                     print('Users : \n')
#
#                     for user in library1.users:
#                         if user.name != admin:
#                             print(f"{user.name} , {len(user.borrowed_books)}, {len(user.returned_books)}")
#
#                 elif ch == 3:
#                     print('Book lists : \n')
#                     for book in library1.books:
#                         print(f"{book.id} \t {book.name} \t {book.quantity}")
#
#                 elif ch == 4:
#                     current_user = None
#
#                 else:
#                     print('Choose a valid option ')
#
#             else:
#                 print('Options for normal users \n')
#                 print('1: Borrow Book')
#                 print('2: Return Book')
#                 print('3: Show all books')
#                 print('4: Show borrowed books')
#                 print('5: Show history')
#                 print('6: Logout')
#
#
#                 ch = int (input('Enter your choice : '))
#                 if ch == 1:
#                     id = int (input('Enter book id : '))
#                     library1.borrow_books(current_user,id)
#
#                 elif ch == 2:
#                     id = int(input('Enter book id : '))
#                     library1.return_book(current_user,id)
#
#                 elif ch == 3:
#                     print('\n All books of this library : \n')
#                     for book in library1.books:
#                         if book in current_user.borrowed_books:
#                             print(f'{book.id} {book.name} Reading now...')
#                         elif book in current_user.returned_books:
#                             print(f"{book.id} {book.name} is already been read...")
#                         else:
#                             print(f"{book.id} {book.name} {book.quantity} Did not read...")
#
#                 elif ch == 4:
#                     print('\n Borrowed books: \n')
#                     for book in current_user.borrowed_books:
#                         print(f'{book.id} {book.name} is borrowed by me')
#
#                 elif ch == 5:
#                     print(f'\History\n')
#                     for book in current_user.returned_books:
#                         print(f'{book.id} , {book.name} I have read')
#
#                 elif ch == 6:
#                     current_user = None
#
#                 else:
#                     print('Choose a valid option')


class Book:

    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity


class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBooks = []
        self.returnedBooks = []


class Library:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.books = []

    def addBook(self, id, name, quantity):

        for book in self.books:
            if book.id == id:
                print(f"\n\t---> !! Book Id {book.id} already exists")
                return

        book = Book(id, name, quantity)
        self.books.append(book)

        print(f"\n\t---> {book.name} X {quantity} added succesfully !")

    def addUser(self, id, name, password):

        for user in self.users:
            if user.id == id:
                print(f"\n\t---> !! User Id {book.id} already exists")
                return

        user = User(id, name, password)
        self.users.append(user)
        return user

    def borrowBook(self, user, token):

        for book in self.books:
            if book.id == token:
                if book in user.borrowedBooks:
                    print("\n\t---> Already borrowed !")
                    return
                elif book.quantity == 0:
                    print("\n\t---> No Copy Available !")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    print(f"\n\t---> Borrowed {book.name} Succesfully !")
                    return

        print(f"\n\t---> Not found any book with id: {token} !")

    def returnBook(self, user, token):

        for book in self.books:
            if book.id == token:
                if book in user.borrowedBooks:
                    book.quantity += 1
                    user.returnedBooks.append(book)
                    user.borrowedBooks.remove(book)
                    print(f"\n\t---> Returned {book.name} Succesfully !")
                    return
                else:
                    print(f"\n\t---> !!! You are not reading {book.name} now")
                    return

        print(f"\n\t---> !!! Not found any book with id: {token}")


bsk = Library("Bishwa Shahitja Kendro")
admin = bsk.addUser(1000, "admin", "admin")
ratin = bsk.addUser(17, "ratin", "123")
cpBook = bsk.addBook(11, "CP book", 5)

currentUser = admin
changeOfUser = True

while True:
    if currentUser == None:
        print("\n\t--->!!! No logged in user\n")

        option = input("Login or Register (L/R) :")

        if option == "L":
            id = int(input("Enter Id:"))
            password = input("Enter Password:")

            match = False
            for user in bsk.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    changeOfUser = True
                    match = True
                    break
            if match == False:
                print("\n\t---> No user Found !\n")

        elif option == "R":
            id = int(input("\tEnter Id:"))
            name = input("\tEnter name:")
            password = input("\tEnter Password:")

            for user in bsk.users:
                if user.id == id:
                    print("\n\t---> User already exists!\n")

            user = bsk.addUser(id, name, password)
            currentUser = user
            changeOfUser = True

    else:
        if changeOfUser:
            print("\n------------------------------------")
            print(f"\tWelcome Back {currentUser.name} !")
            print("------------------------------------")
            changeOfUser = False
        else:
            print("\n\t<---------------------------->")

        if currentUser.name == "admin":

            print("Options:\n")
            print("1: Add book")
            print("2: Show users")
            print("3: Show all books")
            print("4: Logout")

            ch = int(input("\nEnter Option:"))

            if ch == 1:
                id = int(input("\tEnter book id:"))
                name = input("\tEnter book name:")
                quan = int(input("\tEnter No of books:"))

                bsk.addBook(id, name, quan)

            elif ch == 2:
                print("\n\tUsers:\n")
                print(f'\tName\tReading Now\tAlready Read')

                for user in bsk.users:
                    if user.name != "admin":
                        print(f'\t{user.name}\t\t{len(user.borrowedBooks)}\t\t{len(user.returnedBooks)}')


            elif ch == 3:

                print("\n\tBook List:\n")

                for book in bsk.books:
                    print(f'\t{book.id}\t{book.name}\t{book.quantity}')

            elif ch == 4:
                currentUser = None

            else:
                print("\n\t---> !!! Choose Valid Option\n")


        else:
            print("Options:\n")
            print("1: Borrow Book")
            print("2: Return Book")
            print("3: Show All Books")
            print("4: Show Borrowed books")
            print("5: Show History")
            print("6: Logout")

            ch = int(input("\nEnter Option:"))

            if ch == 1:
                id = int(input("\tEnter book id:"))
                bsk.borrowBook(currentUser, id)
            elif ch == 2:
                id = int(input("\tEnter book id:"))
                bsk.returnBook(currentUser, id)

            elif ch == 3:
                print("\n\tAll Books:\n")
                for book in bsk.books:
                    if book in currentUser.borrowedBooks:
                        print(f'\t{book.id}\t{book.name}\t{book.quantity}\tReading Now..')
                    elif book in currentUser.returnedBooks:
                        print(f'\t{book.id}\t{book.name}\t{book.quantity}\tAlready Read')
                    else:
                        print(f'\t{book.id}\t{book.name}\t{book.quantity}\tDid not Read')


            elif ch == 4:
                print("\n\tBorrowed Books:\n")
                for book in currentUser.borrowedBooks:
                    print(f'\t{book.id}\t{book.name}\t{book.quantity}')

            elif ch == 5:
                print("\n\tHistory:\n")
                for book in currentUser.returnedBooks:
                    print(f'\t{book.id}\t{book.name}\t{book.quantity}')

            elif ch == 6:
                currentUser = None

            else:
                print("\n\t---> !!! Choose Valid Option\n")
