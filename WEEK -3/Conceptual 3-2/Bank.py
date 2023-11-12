'''

from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.__password = password

    @abstractmethod
    def introduce_yourself(self):
        pass

    # def get_password(self):
    #     return self.__password

    @property
    def get_pass(self):
        return self.__password

    @get_pass.setter
    def set_pass(self,value):
        self.__password = value

class employee(User):
    def __init__(self,name,email,password):
        super().__init__(name, email, password)

    def introduce_yourself(self):
        print('I am Employee')

class Admin (User):
    def __init__(self,name,email, password):
        super().__init__(name,email, password)

    def introduce_yourself(self):
        print('I am Admin')



admin_1 = Admin('Mizan Chowdhury','mizan@gmail','3445')
# print(admin_1.get_password())
print(admin_1.get_pass)
admin_1.set_pass = '6778'
print(admin_1.get_pass)

'''

from abc import ABC,abstractmethod
class Account(ABC):
    accounts = []
    def __init__(self,name,account_no,password,type):
        self.name = name
        self.account_no = account_no
        self.password = password
        self.type = type

        self.balance = 0
        Account.accounts.append(self)


    @abstractmethod
    def show_info(self):
        pass

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} tk. New balance : {self.balance} tk.")

        else:
            print('Invalid deposit amount')



    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. New Balance : {self.balance} tk")

        else:
            print('Invalid withdrawal amount')





    # method overloading
    # def change_info(self,name,str=''):
    #     self.name = name
    #     print(f"Name has been changed for account no : {self.account_no} .")

    # method overloading

    def change_info(self, name, password=''):
        if password == '':
            self.name = name
            print(f"Name has been changed for account no : {self.account_no} .")
        else:
            self.name = name
            self.password = password
            print(f"Name and password has been changed for account no : {self.account_no} .")
    #         TODO: use getter setter to change password



class Savings_Account(Account):
    def __init__(self,name,account_no,password,interest_rate):
        super().__init__(name,account_no,password,"Savings")
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_money = self.balance * (self.interest_rate / 100)
        print(f"{self.interest_rate} % interest applied")
        self.deposit(interest_money)

    def show_info(self):
        print(f"Information of {self.type} account of {self.name}")
        print(f"Account Type : {self.type}")
        print(f"Owners's name : {self.name}")
        print(f"Account No : {self.account_no}")
        print(f"Current Balance : {self.balance}")
        print()




class Special_Account(Account):
    def __init__(self,name,account_no,password,limit):
        super().__init__(name,account_no,password,"Special")
        self.limit = limit
        self.remaining_limit = limit

    def show_info(self):
        print(f"Information of {self.type} account of {self.name}")
        print(f"Account Type : {self.type}")
        print(f"Owners's name : {self.name}")
        print(f"Account No : {self.account_no}")
        print(f"Current Balance : {self.balance}")
        print()

    # method overriding (parent class er upore matobbori kortesi)
    def withdraw(self,amount):

        '''
        case 1 : balance 2000 tk. withdraw korte chai 1000 tk
        case 2 : balance 2000 tk. withdraw korte chai 2500 tk
        csee 3 : balance 0 tk. withdraw korte chai 500 tk
        '''
        if amount> 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdraw {amount} tk. New Balance : {self.balance} tk')

            elif self.balance < amount and (amount-self.balance) <= self.limit:
                self.balance -= amount
                self.remaining_limit = self.remaining_limit - amount
                print(f'Withdraw {amount} tk. New Balance : {self.balance} tk')




    # main


current_user = None
while(True):
    if current_user == None:
        print('No Logged in user ')
        ch = input('Register / Login (R/L): ')
        if ch.upper() == 'R':
            # if someone wants to register
            name = input('Enter name : ')
            account_no = input('Enter Account No. : ')
            password = input('Enter Password : ')
            type = input('Savings or Special Account (SV/SP): ')

            if type.upper() == 'SV':
                # savings account
                interest_rate = int(input('Enter interest rate: '))
                current_user = Savings_Account(name,account_no,password,interest_rate)

            else:
                #       Special Account
                limit = int(input('Enter limit : '))
                current_user = Special_Account(name,account_no,password,limit)

        else:
            # if someone wants to log in
            acc_no = int(input('Enter account no. : '))
            for account in Account.accounts:
                if account.account_no == acc_no:
                    current_user = account
                    break

    else:
        # may be any logged-in user
        print()
        print(f"Welcome {current_user.name} ")

        if current_user.type.lower() == 'savings':
            print('1 : Withdraw')
            print('2 : Deposit')
            print('3 : Show Info')
            print('4 : Change Info')
            print('5 : Apply Interest')
            print('6 : Logout')
            print()

            op = int(input('Enter option : '))

            if op == 1:
                amount = int(input('Enter amount to withdraw : '))
                current_user.withdraw(amount)

            elif op == 2:
                amount = int(input('Enter amount to deposit : '))
                current_user.deposit(amount)

            elif op == 3:
                current_user.show_info()

            elif op == 4:
                new_name = input('Enter new name : ')
                current_user.change_info(new_name)

            elif op == 5:
                current_user.apply_interest()

            elif op == 6:
                current_user = None
                print('Log out Successfull')
                print()

            else:
                print('Invalid Option')

        else:
            # if current user is a special account holder
            print('1 : Withdraw')
            print('2 : Deposit')
            print('3 : Show Info')
            print('4 : Change Info ')
            print('5 : Logout')
            print()

            op = int(input('Enter Option : '))

            if op == 1:
                withdraw_amount = int(input('Enter amount to withdraw : '))
                current_user.withdraw(withdraw_amount)

            elif op == 2:
                deposit_amount = int(input('Enter amount to deposit : '))
                current_user.deposit(deposit_amount)

            elif op == 3:
                current_user.show_info()

            elif op == 4:
                new_name = input('Enter new name : ')
                new_pass = input('Enter new password : ')
                current_user.change_info(new_name,new_pass)




            elif op == 5:
                current_user = None
                print('Log out Successfull')
                print()

            else:
                print('Invalid option ')
