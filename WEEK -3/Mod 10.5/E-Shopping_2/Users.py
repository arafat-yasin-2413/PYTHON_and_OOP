'''
Uml design

https://drive.google.com/file/d/1hk_LYL1Q7_cg-D6-9NrOQD7EgcwudLaN/view?usp=sharing
https://shorturl.at/bFLSV
'''


from abc import ABC,abstractmethod
class User(ABC):
    user_list = []
    def __init__(self,name,email,password,type):
        self.name = name
        self.email = email
        self.__password = password
        self.type = type

        User.user_list.append(self)
        self.length = len(User.user_list)


    @abstractmethod
    def show_profile(self):
        pass

    @classmethod
    def create_account(cls,name,email,password,type):
        if type.upper() == 'CUSTOMER':
            return Customer(name,email,password)
        elif type.upper() == 'SELLER':
            return Seller(name, email, password)

    def show_all_user_based_on_type(self):
        for user in User.user_list:
            if user.type.upper() == 'SELLER':
                user.show_profile()

            elif user.type.upper() == 'CUSTOMER':
                user.show_profile()

    def get_password(self):
        return self.__password


class Customer(User):
    customer_list = []
    def __init__(self,name,email,password):
        super().__init__(name, email, password,'customer')
        Customer.customer_list.append(self)

    def show_profile(self):
        print(f"Customer's name : {self.name}, email : {self.email}")

    def show_customer_list(self):
        for customer in Customer.customer_list:
            customer.show_profile()


class Seller(User):
    seller_list = []
    def __init__(self,name,email,password):
        super().__init__(name, email, password,'seller')
        Seller.seller_list.append(self)


    def show_profile(self):
        print(f"Seller's name : {self.name}, email : {self.email}")

    def show_seller_list(self):
        for seller in Seller.seller_list:
            seller.show_profile()


#  --------------------------------------Product Segment starts ------------------------




#  --------------------------------------Product Segment ends ------------------------



# main


current_user = None
while(True):
    print()
    print('1. Register account ')
    print('2. See total user ')
    print('3. Login account ')
    print('4. Exit ')

    opt = int(input('Enter option : '))
    if opt == 1:
        # Registering
        ch = input('Register as Seller/Customer (S/C) : ')
        if ch.upper() == 'S':
            # Registering as seller
            print()
            print('Registering as seller...')
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter password : ')
            Seller.create_account(name,email, password,'seller')
            # Seller(name,email, password)
            print(f"Successfully registered #{name} as a seller")
            # print(f"total user : {len(User.user_list)}")

        elif ch.upper() == 'C':
            # Registering as customer
            print()
            print('Registering as customer...')
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter password : ')
            Customer.create_account(name, email, password,'customer')
            # Customer(name, email, password)
            print(f"Successfully registered #{name} as a customer")

    elif opt == 2:
        print(f"total user : {len(User.user_list)}")


    elif opt == 3:
        # Login account...
        pass

    elif opt == 4:
        break
