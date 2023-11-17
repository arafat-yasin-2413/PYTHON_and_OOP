'''



'''

from abc import ABC, abstractmethod


class User:
    def __init__(self, name, email, password, address):
        self.name = name
        self.email = email
        self.__password = password
        self.address = address

    def get_password(self):
        return self.__password


class Account(ABC, User):
    account_list = []

    def __init__(self, name, email, password, address, acc_type):
        super().__init__(name, email, password, address)
        self.acc_type = acc_type

        self.__history = []  # TODO: should not be public

        self.__balance = 0

        self.__loan_count = 0
        self.__loan_taken = 0  # in taka

        self.sent_money = 0
        self.received_money = 0

        if acc_type.lower() == 'savings':
            self.digit = 1001 + len(Account.account_list)
            self.acc_number = 's' + str(self.digit)

        elif acc_type.lower() == 'current':
            self.digit = 1001 + len(Account.account_list)
            self.acc_number = 'c' + str(self.digit)

    def get_balance(self):
        return self.__balance

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

    # ---------------------------------------------Functionalities--------------------------------------------
    # general functionalities
    def deposit_amount(self, amount):
        deposit_history = ""
        if amount > 0:
            self.__balance += amount
            deposit_history = f"Deposited {amount} tk"
            self.__history.append(deposit_history)
        print(f"{self.name} sir/madam , Deposit {amount} tk successfull")

    def withdraw_amount(self, amount):
        withdraw_history = ""
        if amount > self.__balance:
            print("Withdrawal amount exceeded")
        elif amount <= self.__balance:
            self.__balance -= amount
            withdraw_history = f"Withdraw {amount} tk"
            self.__history.append(withdraw_history)
            print(f"Withdraw {amount} tk Successfull")

    def check_available_balance(self):
        print(f"{self.name} ({self.acc_number}) current balance : {self.__balance} tk. ")

    def get_transaction_history(self):
        for hist in self.__history:
            print(hist)

    def take_loan(self, user, loan_amount):
        loan_history = ""
        if self.__loan_count < 2:
            print()
            print(f"Loan Taken {loan_amount} tk from bank.")
            loan_history = f"Loan taken {loan_amount} tk "
            self.__history.append(loan_history)
            self.__balance += loan_amount
            self.__loan_taken += loan_amount
            self.__loan_count += 1
            print(f"{user.name} ({user.acc_number}) has total loan : {self.__loan_taken} tk")

        elif self.__loan_count >= 2:
            print(f"No More Loan. Repay First")
            # TODO: Repaying the debt and taking loan again for another two times

    def get_loan_taken(self):
        return self.__loan_taken

    def transfer_money(self, sending_amount, sender):
        sender_transferring_money = ""
        receiver_receiving_money = ""

        if sender.__balance >= sending_amount:
            # porjapto taka ache
            receiver_acc_num = input('Enter Receiver Account No : ')
            is_receiver_found = False
            for user in Account.account_list:
                if user.acc_number == receiver_acc_num:
                    is_receiver_found = True
                    print(f"Receiver ({user.name}) has been found successfully")
                    user.received_money += sending_amount
                    sender.sent_money += sending_amount
                    sender.__balance -= sending_amount
                    sender_transferring_money = f"Transferred {sending_amount} tk to {user.name} "
                    receiver_receiving_money = f"Received {sending_amount} tk from {sender.name} "
                    sender.__history.append(sender_transferring_money)
                    user.__history.append(receiver_receiving_money)
                    print(f"Money Transfer Successfull, {sending_amount} tk to {user.name} ")

            if not is_receiver_found:
                print("Account does not exist")
        else:
            print(f"You have not sufficient money in your account")


# ------------------- DONE ----------------- DONE ------------------- DONE ----------------- DONE -----------------
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

        self.is_bankrupt = False
        self.is_loan_active = False

    def show_profile(self):
        print(f"This is *{self.name}* bank")
        print(f"Total number of user :  {len(Account.account_list)}")


class Admin(Bank):
    admin_list = []

    def __init__(self, name, email, password, acc_type):
        self.digit_part = None
        self.admin_id = Admin.set_admin_id()

        self.name = name
        self.email = email
        self.__password = password
        self.acc_type = acc_type

        Admin.admin_list.append(self)




    @classmethod
    def set_admin_id(cls):
        digit_part = len(Admin.admin_list) + 101
        ac_num = 'admin' + '-' + str(digit_part)
        return ac_num
    
    def get_password(self):
        return self.__password

    def show_admin_profile(self):
        print(f"This is Admin with id : {self.admin_id}")

    # admin can see user list


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
        acc_type = input('Enter account type [ admin or (s/c)] ? : ')

        if acc_type.lower() == 'admin':
            account_type = 'admin'
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter password : ')
            admin_obj = Admin(name, email, password, acc_type)
            print(f"ADMIN {name} Account Created Successfully. ")


        elif acc_type.lower() == 's':
            account_type = 'savings'
            name = input('Enter name : ')
            email = input('Enter email : ')
            password = input('Enter password : ')
            address = input('Enter address : ')

            Account.create_account(name, email, password, address, account_type)
            print(f"{name}'s ({account_type}) account created successfully ")


        elif acc_type.lower() == 'c':
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
        choice = input('Log in as (admin/user)? : ')


        if choice.lower() == 'admin':
            print(f'Logging in as {choice} ...')
            email = input('Enter email : ')
            password = input('Enter password : ')

            # ADMIN parts
            current_admin = None
            is_admin_matched = False
            for admin in Admin.admin_list:
                if admin.email == email and admin.get_password() == password:
                    is_admin_matched = True
                    print('Admin matched')
                    print(f"WELCOME admin {admin.name} ({admin.admin_id}) ")
                    current_admin = admin

            if is_admin_matched == False:
                print("Admin didn't match")

            if current_admin != None:
                while True:
                    print()
                    print('1. Show Admin Profile ')
                    print('2. Logout')
                    print()

                    admin_option = int(input('Enter admin option : '))

                    if admin_option == 1:
                        current_admin.show_admin_profile()

                    elif admin_option == 2:
                        print(f"Admin : {current_admin.name} Logged Out Successfully ")
                        current_admin = None
                        break

        elif choice.lower() == 'user':
            print(f"Logging in as {choice} ...")
            email = input('Enter email : ')
            password = input('Enter password : ')

            # USER parts
            current_user = None
            user_matched = False
            for user in Account.account_list:
                if email == user.email and password == user.get_password():
                    user_matched = True
                    current_user = user
                    print(f"\nWelcome {user.name} ({user.acc_type})")
                    break

            if not user_matched:
                print('No User Account has been found')

            if current_user is not None:
                while True:
                    print()
                    print('1. Deposit Money')
                    print('2. Withdraw Money')
                    print('3. Check Available Balance ')
                    print('4. See Transaction History ')
                    print('5. Take Loan ')
                    print('6. Transfer Money')
                    print('7. Show Current Loan Amount ')
                    print('8. Log Out ')
                    print()

                    opt = int(input('Enter option : '))
                    if opt == 1:
                        # Deposit money
                        print('Deposit in progress ...')
                        d_amount = int(input('Enter amount : '))
                        if d_amount < 0:
                            print('Amount should be > 0 ')
                        elif d_amount > 0:
                            current_user.deposit_amount(d_amount)
                        # TODO: if user gives alphabets by mistake


                    elif opt == 2:
                        # Withdraw money
                        print('Withdraw in progress ...')

                        w_amount = int(input('Enter amount : '))
                        current_user.withdraw_amount(w_amount)


                    elif opt == 3:
                        # Check available balance
                        current_user.check_available_balance()



                    elif opt == 4:
                        # See Transaction history
                        print(f'--------- History of {current_user.name} ({current_user.acc_number}) ---------')
                        current_user.get_transaction_history()
                        print(f"----------------------------------------------")


                    elif opt == 5:
                        # Take Loan
                        print('Loan taking from bank ...')
                        loan_amount = int(input('Enter loan amount : '))
                        current_user.take_loan(current_user, loan_amount)

                    elif opt == 6:
                        # Transfer money
                        print('Money Transfer in progress ...')
                        print(f"Sender : {current_user.name} ({current_user.acc_number}) ")
                        sending_money = int(input('Enter amount to send : '))
                        current_user.transfer_money(sending_money, current_user)


                    elif opt == 7:
                        # Showing current loan amount
                        print(f"Current Loan : {current_user.get_loan_taken()} tk of {current_user.name}")

                    elif opt == 8:
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
