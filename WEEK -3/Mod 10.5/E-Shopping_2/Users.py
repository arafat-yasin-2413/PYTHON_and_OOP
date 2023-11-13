'''
Uml design

https://drive.google.com/file/d/1hk_LYL1Q7_cg-D6-9NrOQD7EgcwudLaN/view?usp=sharing
https://shorturl.at/bFLSV

https://shorturl.at/dhL05
'''

from abc import ABC,abstractmethod


''' -------------------------------------Product Segment------------------------------------------'''












''' -------------------------------------Product Segment Ends------------------------------------------'''


class User(ABC):
    user_list = []
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.__password = password

    def create_account(self,name,email,password,type):
        if type.upper() == "CUSTOMER":
            cust_obj = Customer(name, email, password,type)
            User.user_list.append(cust_obj)
            return cust_obj

        elif type.upper() == "SELLER":
            seller_obj = Seller(name, email, password,type)
            User.user_list.append(seller_obj)
            return seller_obj

    @abstractmethod
    def show_profile(self):
        raise NotImplementedError


    def get_password(self):
        return self.__password


class Customer(User):
    def __init__(self,name,email,password,type):
        super().__init__(name, email, password)
        self.type = type

    def show_profile(self):
        print(f"Customer's name : {self.name}, email : {self.email}")

class Seller(User):
    def __init__(self,name,email,password,type):
        super().__init__(name, email, password)
        self.type = type

    def show_profile(self):
        print(f"Seller's name : {self.name}, email : {self.email}")


class E_Shopping(User):
    def __init__(self,name):
        self.customer_list = []
        self.name = name
        self.seller_list = []

    def show_profile(self):
        print(f"This is E-Shopping site {self.name}")
        print(f"Total no. sellers : {len(self.seller_list)}")
        print(f"Total no. customers : {len(self.customer_list)}")


daraz = E_Shopping('Daraz Bd')

# main starts


while(True):
    print()
    print('1. Create Account')
    print('2. Login Account')
    print('3. Show Sellers and Customers  ')
    print('4. Show User List ')
    print('5. Exit')

    ch = int(input('Enter your Choice : '))
    if ch == 1:
        account_type = input('Account type ? : ')

        if account_type.upper() == 'SELLER':

            print('Creating an account as Seller...')
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter Password : ')
            s_obj = daraz.create_account(name, email, password,account_type)
            daraz.seller_list.append(s_obj)
            print(f'Successfully Registered as a Seller')
            s_obj.show_profile()

        elif account_type.upper() == "CUSTOMER":

            print('Creating an account as Customer...')
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter Password : ')
            c_obj = daraz.create_account(name, email, password, account_type)
            daraz.customer_list.append(c_obj)
            print(f'Successfully Registered as a Customer')
            c_obj.show_profile()


    elif ch == 2:
        # Log in part

        email = input('Enter email : ')
        password = input('Enter password : ')
        for user in daraz.user_list:
            # user.show_profile()
            if user.email == email and user.get_password() == password:
                print()
                print(f'Welcome {user.name} and type : {user.type}')





    elif ch == 3:
        daraz.show_profile()

    elif ch == 4:
        # print(daraz.user_list)
        for user in daraz.user_list:
            user.show_profile()

    elif ch == 5:
        break


