'''
Uml design

https://drive.google.com/file/d/1hk_LYL1Q7_cg-D6-9NrOQD7EgcwudLaN/view?usp=sharing
https://shorturl.at/bFLSV

https://shorturl.at/dhL05
'''

from abc import ABC, abstractmethod

''' -------------------------------------Product Segment------------------------------------------'''


class Product(ABC):
    product_list = []

    def __init__(self, id,name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        # Product.product_list.append(self)

    @abstractmethod
    def show_info(self):
        raise NotImplementedError

    def add_products_to_inventory(self, product_obj):
        Product.product_list.append(product_obj)
        print(f'{product_obj.name} added successfully')


class Phone(Product):
    def __init__(self, id, name, price, quantity, color):
        super().__init__(id, name, price, quantity)
        self.color = color

    def show_info(self):
        if self.quantity > 0:
            print(f"{self.name} -- {self.id} ---- {self.price} tk ------ {self.quantity}")


class Laptop(Product):
    def __init__(self, id, name, price, quantity, color):
        super().__init__(id, name, price, quantity)
        self.color = color

    def show_info(self):
        if self.quantity > 0:
            print(f"{self.name} -- {self.id} ---- {self.price} tk ------ {self.quantity}")


class Keyboard(Product):
    def __init__(self, id, name, price, quantity, color):
        super().__init__(id, name, price, quantity)
        self.color = color

    def show_info(self):
        if self.quantity > 0:
            print(f"{self.name} -- {self.id} ---- {self.price} tk ------ {self.quantity}")


# creating products
nokia_1 = Phone(110,"Nokia 1180", 2400, 10, 'Blue')
samsung_f32 = Phone(111,"Samsung F32", 12000, 12, 'Black')
samsung_a52 = Phone(112,'Samsung A52', 16000, 15, 'Black')

mac_13 = Laptop(210,'Macbook Air 13', 30000, 20, 'Space Gray')
mac_14 = Laptop(211,'Macbook Air 14', 35000, 16, 'Midnight Blue')
mac_15 = Laptop(212,'Macbook Air 15', 45000, 18, 'Silvery night')

a4tech_1 = Keyboard(310,'FG 1010', 1500, 6, 'Orange')
a4tech_2 = Keyboard(311,'FG 2322', 1800, 10, 'Black')
a4tech_3 = Keyboard(312,'FG 7543', 2000, 14, 'Black')

''' -------------------------------------Product Segment Ends------------------------------------------'''


class User(ABC):
    user_list = []

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password

    def create_account(self, name, email, password, type):
        if type.upper() == "CUSTOMER":
            cust_obj = Customer(name, email, password, type)
            User.user_list.append(cust_obj)
            return cust_obj

        elif type.upper() == "SELLER":
            seller_obj = Seller(name, email, password, type)
            User.user_list.append(seller_obj)
            return seller_obj

    @abstractmethod
    def show_profile(self):
        raise NotImplementedError

    def get_password(self):
        return self.__password


class Customer(User):
    def __init__(self, name, email, password, type):
        super().__init__(name, email, password)
        self.type = type


    def show_profile(self):
        print(f"Customer's name : {self.name}, email : {self.email}")

    def show_cart(self,lst):
        for obj in lst:
            print(f'{obj.name} only at : {obj.price} tk')

    def show_bill_amount(self,lst):
        total = 0
        for obj in lst:
            # print(obj.price)
            # print(type(obj.price))
            total += obj.price
        print(f"{self.name}, Your total bill is {total} tk")

class Seller(User):
    def __init__(self, name, email, password, type):
        super().__init__(name, email, password)
        self.type = type
        self.seller_product = []

    def show_profile(self):
        print(f"Seller's name : {self.name}, email : {self.email}")


class E_Shopping(User, Product):
    def __init__(self, name):
        self.customer_list = []
        self.name = name
        self.seller_list = []
        self.revenue = 0
        self.balance = 0

        self.receiveable_amount = 0

    def show_profile(self):
        print(f"This is E-Shopping site {self.name}")
        print(f"Total no. sellers : {len(self.seller_list)}")
        print(f"Total no. customers : {len(self.customer_list)}")

    def show_info(self):
        pass

    def calculate_amount(self,cust,order_list):
        total = 0
        for objct in order_list:

            if objct.quantity >= 1:
                objct.quantity -= 1
                total += objct.price
            elif objct.quantity == 0:
                print(f"{objct.name}({objct.id}) is not available now")

        self.receiveable_amount = total
        print(f"{cust.name} Sir/Madam You Have to Pay {self.receiveable_amount} tk")
        # print(f"{cust.name} sir/madam , you have to pay {total} tk")




    def checkout(self,curr_cust,amount):
        if amount == self.receiveable_amount:
            self.revenue += self.receiveable_amount
            self.balance += self.receiveable_amount

            print(f"Here is your Products")
            print(f"Thank You ->  {curr_cust.name} for shopping with {self.name}")
            print()

        elif amount > self.receiveable_amount:
            self.revenue += self.receiveable_amount
            self.balance += self.receiveable_amount

            print(f"Here is your change {amount - self.receiveable_amount} tk {curr_cust.name} Sir/Madam")
            print(f"Here is your Products")
            print(f"Thank You ->  {curr_cust.name} for shopping with {self.name}")
            print()

        else:
            print(f"{curr_cust.name} Sir/Madam PLEASE PAY {self.receiveable_amount - amount} TK MORE TO PROCEED ! ")
            print()


daraz = E_Shopping('Daraz Bd')

# main starts


while (True):
    print()
    print('1. Create Account')
    print('2. Login Account')
    print('3. Show Sellers and Customers  ')
    print('4. Show User List ')
    print('5. Exit')

    ch = int(input('Enter your Choice : '))
    if ch == 1:
        # Creating an account
        account_type = input('Account type ? : ')

        if account_type.upper() == 'SELLER':

            print('Creating an account as Seller...')
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter Password : ')
            s_obj = daraz.create_account(name, email, password, account_type)
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
                if user.type.upper() == "SELLER":

                    print()
                    print(f'Welcome {user.name}    ({user.type})')
                    current_seller = user
                    while (True):
                        print('\t 1. Add Products')
                        print('\t 2. Seeing my products')
                        print('\t 3. Log out')

                        option = int(input('Enter your option seller : '))
                        if option == 1:
                            # print(f"Seller {user.name} is adding products")
                            daraz.add_products_to_inventory(nokia_1)
                            daraz.add_products_to_inventory(samsung_f32)
                            daraz.add_products_to_inventory(samsung_a52)

                            daraz.add_products_to_inventory(mac_13)
                            daraz.add_products_to_inventory(mac_14)
                            daraz.add_products_to_inventory(mac_15)

                            daraz.add_products_to_inventory(a4tech_1)
                            daraz.add_products_to_inventory(a4tech_2)
                            daraz.add_products_to_inventory(a4tech_3)










                        elif option == 2:
                            # print(f"Seller {user.name} Seeing my products")
                            for product in daraz.product_list:
                                product.show_info()

                        elif option == 3:
                            print(f'{user.name} Logged Out Successfully')
                            print()
                            break


                elif user.type.upper() == "CUSTOMER":
                    print()
                    print(f'Welcome {user.name}    ({user.type})')

                    current_cust = user
                    my_cart = []
                    while (True):
                        print('\t 1. See all products')
                        print('\t 2. Add to cart')
                        print('\t 3. Show my cart ')
                        print('\t 4. Show bill amount ')
                        print('\t 5. Place Order')
                        print('\t 6. Pay Bill')
                        print('\t 7. Logout')
                        print()

                        opt = int(input('Enter your choice customer : '))
                        if opt == 1:
                            # print(f'I am {current_user.name} seeing all products')
                            for product in daraz.product_list:
                                product.show_info()

                        elif opt == 2:
                            # print(f"I am {current_cust.name} adding product to my cart")
                            p_id = int(input('enter product id : '))
                            for obj in daraz.product_list:
                                if p_id == obj.id:
                                    my_cart.append(obj)

                        elif opt == 3:
                            # for p_obj in my_cart:
                            #     print(p_obj.name)
                            current_cust.show_cart(my_cart)

                        elif opt == 4:
                            current_cust.show_bill_amount(my_cart)

                        elif opt == 5:
                            # placing order
                            daraz.calculate_amount(current_cust,my_cart)

                        elif opt == 6:
                            amount = int(input('Enter amount to pay : '))
                            daraz.checkout(current_cust,amount)
                            my_cart.clear()


                        elif opt == 7:
                            print(f'{current_cust.name} Logged Out Successfully')
                            print()
                            break


            else:
                pass



    elif ch == 3:
        daraz.show_profile()

    elif ch == 4:
        for user in daraz.user_list:
            user.show_profile()

    elif ch == 5:
        break
