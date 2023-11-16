# class BankAccount:
#     # Class variable to keep track of the last assigned account number
#     last_account_number = 1000
#
#     def __init__(self, name, email, address, password):
#         self.name = name
#         self.email = email
#         self.address = address
#         self.password = password
#         # Automatically generate account number
#         self.account_number = BankAccount.generate_account_number()
#
#     @classmethod
#     def generate_account_number(cls):
#         # Increment the last account number and return the new one
#         cls.last_account_number += 1
#         return cls.last_account_number
#
# # Example usage
# user1 = BankAccount("John Doe", "john@example.com", "123 Main St", "password123")
# print(f"User 1 Account Number: {user1.account_number}")
#
# user2 = BankAccount("Jane Doe", "jane@example.com", "456 Oak St", "securepass")
# print(f"User 2 Account Number: {user2.account_number}")


'''



'''

from abc import ABC, abstractmethod


class Account(ABC):
    account_list = []

    def __init__(self, name, email, password, address, acc_type):
        self.name = name
        self.email = email
        self.__password = password
        self.address = address
        self.acc_type = acc_type

        if acc_type.lower() == 'savings':
            self.digit = 1001 + len(Account.account_list)
            self.acc_number = 's' + str(self.digit)

        elif acc_type.lower() == 'current':
            self.digit = 1001 + len(Account.account_list)
            self.acc_number = 'c' + str(self.digit)

        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def get_password(self):
        return self.__password

    @classmethod
    def create_account(self, name, email, password, address, acc_type):
        if acc_type.lower() == "savings":
            sv_user = Savings_Account(name, email, password, address)
            Account.account_list.append(sv_user)

        elif acc_type.lower() == "current":
            curr_user = Current_Account(name, email, password, address)
            Account.account_list.append(curr_user)

    @abstractmethod
    def show_profile(self):
        raise NotImplementedError

    def show_user_list(self):
        for user in Account.account_list:
            user.show_profile()

    # general functionalities
    def deposit_amount(self, amount):
        if amount > 0:
            self.__balance += amount
        print(f"{self.name} sir/madam , Deposit {amount} tk successfull")

    def withdraw_amount(self):
        pass

    def check_available_balance(self):
        print(f"{self.name} ({self.acc_number}) current balance : {self.__balance} tk. ")

    def transaction_history(self):
        # string format a ekta list er vitore rakha jete pare
        # just normal sentence with description
        pass

    def take_loan(self):
        pass

    def transfer_money(self):
        pass


class Savings_Account(Account):
    def __init__(self, name, email, password, address):
        super().__init__(name, email, password, address, "savings")

    def show_profile(self):
        print(f"Owner's name : {self.name} , A/c Number : {self.acc_number} and A/c type : {self.acc_type}")


class Current_Account(Account):
    def __init__(self, name, email, password, address):
        super().__init__(name, email, password, address, "current")

    def show_profile(self):
        print(f"Owner's name : {self.name} , A/c Number : {self.acc_number} and A/c type : {self.acc_type}")


class Bank(Account):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show_profile(self):
        print(f"This is *{self.name}* bank")
        print(f"Total number of user :  {len(Account.account_list)}")


# --------------------------------------------------------------------------------------
# main starts

dutch_bangla = Bank("Dutch Bangla BD", 'Motijheel, Dhaka')

while (True):
    print()
    print('1. Create Account ')
    print('2. Log in ')
    print('3. Show Users List ')
    print('4. Exit ')
    print()

    ch = int(input('Enter your choice : '))

    if ch == 1:
        # creating an account
        acc_type = input('Enter account type (sv/curr)? : ')

        if acc_type.lower() == 'sv':
            account_type = 'savings'
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter password : ')
            address = input('Enter address : ')

            Account.create_account(name, email, password, address, account_type)
            print(f"{name}'s ({account_type}) account created successfully ")


        elif acc_type.lower() == 'curr':
            account_type = 'current'
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter password : ')
            address = input('Enter address : ')

            Account.create_account(name, email, password, address, account_type)
            print(f"{name}'s ({account_type}) account created successfully ")

    elif ch == 2:
        # Log in
        print('Logging in ...')

        email = input('Enter email : ')
        password = input('Enter password : ')

        current_user = None

        user_matched = False
        for user in Account.account_list:
            if email == user.email and password == user.get_password():
                user_matched = True
                current_user = user
                print(f"\nWelcome {user.name} ({user.acc_type})")
                break

        if not user_matched:
            print('No Account has been found')

        if current_user is not None:
            while True:
                print()
                print('1. Deposit Money')
                print('2. Withdraw Money')
                print('3. Check Available Balance ')
                print('4. See Transaction History ')
                print('5. Take Loan ')
                print('6. Transfer Money')
                print('7. Log Out ')
                print()

                opt = int(input('Enter option : '))
                if opt == 1:
                    # Deposit money
                    print('Deposit in progress ...')
                    amount = int(input('Enter amount : '))
                    if amount < 0:
                        print('Amount should be > 0 ')
                    elif amount > 0:
                        current_user.deposit_amount(amount)

                elif opt == 2:
                    # Withdraw money
                    pass

                elif opt == 3:
                    # Check available balance
                    current_user.check_available_balance()



                elif opt == 4:
                    # See Transaction history
                    pass

                elif opt == 5:
                    # Take Loan
                    pass

                elif opt == 6:
                    # Transfer money
                    pass

                elif opt == 7:
                    # Logout
                    print(f"{current_user.name} ({current_user.acc_number}) Logged Out Successfully")
                    current_user = None
                    break


                else:
                    print(f"Invalid Option ")
    elif ch == 3:
        for user in Account.account_list:
            user.show_profile()

    elif ch == 4:
        break

    else:
        print('Invalid Choice!')
