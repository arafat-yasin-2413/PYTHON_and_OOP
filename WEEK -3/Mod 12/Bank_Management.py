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

        self.__sent_money = 0
        self.__received_money = 0

        if acc_type.lower() == 'savings':
            self.digit = 1001 + len(Account.account_list)
            self.acc_number = 's' + str(self.digit)

        elif acc_type.lower() == 'current':
            self.digit = 1001 + len(Account.account_list)
            self.acc_number = 'c' + str(self.digit)

    def get_sent_money(self):
        return self.__sent_money

    def get_received_money(self):
        return self.__received_money

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

            dutch_bangla.update_revenue(amount)
            dutch_bangla.update_available_balance(amount, 'deposit')
        print(f"{self.name} sir/madam , Deposit {amount} tk successfull")

    def withdraw_amount(self, amount, bankruptcy):
        withdraw_history = ""
        if amount > self.__balance:
            if bankruptcy == True:
                print(f"Withdrawal amount exceeded? Bank gone Bankrupted.")
            else:
                print("Withdrawal amount exceeded")

        elif amount <= self.__balance:
            if bankruptcy == True:
                print(f"Bank has gone BANKRUPTCY. You Can not Withdraw your deposited Money.")
            else:
                self.__balance -= amount
                withdraw_history = f"Withdraw {amount} tk"
                self.__history.append(withdraw_history)
                print(f"Withdraw {amount} tk Successfull")
                dutch_bangla.update_available_balance(amount, 'withdraw')

    def check_available_balance(self):
        print('-----------------------------------------------------------------')
        print(f"{self.name} ({self.acc_number}) current balance : {self.__balance} tk. ")
        print('-----------------------------------------------------------------')

    def get_transaction_history(self):
        for hist in self.__history:
            print(hist)

    def take_loan(self, user, loan_amount, loan_active):
        loan_history = ""
        if self.__loan_count < 2:
            if loan_active == False:
                print(f"We are not giving loan now.")
            else:
                print()
                print(f"Loan Taken {loan_amount} tk from bank.")
                loan_history = f"Loan taken {loan_amount} tk "
                self.__history.append(loan_history)
                self.__balance += loan_amount
                self.__loan_taken += loan_amount
                self.__loan_count += 1
                print(f"{user.name} ({user.acc_number}) has total loan : {self.__loan_taken} tk")
                dutch_bangla.update_available_balance(loan_amount, 'loan giving')
                dutch_bangla.update_given_loan(loan_amount)

        elif self.__loan_count >= 2:
            print(f"No More Loan. You have taken Loan 2 times. ")

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
                    user.__received_money += sending_amount
                    user.__balance += sending_amount
                    sender.__sent_money += sending_amount
                    sender.__balance -= sending_amount
                    sender_transferring_money = f"Transferred {sending_amount} tk to {user.name} "
                    receiver_receiving_money = f"Received {sending_amount} tk from {sender.name} "
                    sender.__history.append(sender_transferring_money)
                    user.__history.append(receiver_receiving_money)
                    print(f"Money Transfer Successfull, {sending_amount} tk to {user.name} ")

            if not is_receiver_found:
                print("\tAccount does not exist")
        else:
            print(f"\tYou have not sufficient money in your account")


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

        self.__revenue = 0
        self.__available_balance = 0
        self.__given_loan = 0

        self.is_bankrupt = False
        self.is_loan_active = True

    def show_profile(self):
        print(f"This is *{self.name}* bank")
        print(f"Total number of user :  {len(Account.account_list)}")

    def get_available_balance(self):
        return self.__available_balance

    def get_given_loan(self):
        return self.__given_loan

    def get_revenue(self):
        return self.__revenue

    def update_revenue(self, amount):
        self.__revenue += amount

    def update_available_balance(self, amount, operation_type):
        if operation_type.lower() == 'deposit':
            self.__available_balance += amount
        elif operation_type.lower() == 'withdraw':
            self.__available_balance -= amount
        elif operation_type.lower() == 'loan giving':
            self.__available_balance -= amount

    def update_given_loan(self, amount):
        self.__given_loan += amount


class Admin(Bank, Account):
    admin_list = []

    def __init__(self, name, email, password, acc_type):
        # super(Bank, self).__init__()
        # super(Account, self).__init__()

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
        print(f"This is Admin {self.name} :: with id : {self.admin_id}")

    # admin can see user list
    def see_all_users(self):
        if not Account.account_list:
            print(f"--------------------------------------------------")
            print(f"\tThere is no Account in the Bank")
            print(f"--------------------------------------------------")
        else:
            print(f"--------------------- Accounts in the Bank --------------------------")
            for user in Account.account_list:
                user.show_profile()
            print('----------------------------------------------------------------------')

    def delete_any_user(self, account_id):
        user_found = False
        user_to_delete = None
        for user in Account.account_list:
            if user.acc_number == account_id:
                user_found = True
                user_to_delete = user

        if user_found == True:
            Account.account_list.remove(user_to_delete)
            print(f"Deleted {user_to_delete.name} :: {user_to_delete.acc_number}")

        else:
            print("\tUser Account not found")

    def check_balance(self):
        self.get_available_balance()


# --------------------------------------------------------------------------------------
# main starts

dutch_bangla = Bank("Dutch Bangla BD", 'Motijheel, Dhaka')
# print(dutch_bangla.__dir__())
admin_1 = Admin('Sifat', 'mail', 'admin1234', 'admin')

Admin.admin_list.append(admin_1)
current_admin = None

# main starts ---------------------------------------------------------------- main starts

while True:
    print()
    print('1. Admin ')
    print('2. User ')
    print('3. Exit ')

    main_opt = int(input('Enter main option : '))

    if main_opt == 1:
        print('Welcome to Admin Operations ')
        while True:
            print()
            print('1. Log in as Admin ')
            print('2. Exit ')

            opt = int(input('Enter option : '))
            if opt == 1:
                # Log in as admin
                print('Logging in as ADMIN ... ')
                print()
                email = input('Enter email : ')
                password = input('Enter password : ')

                is_admin_matched = False
                for admin in Admin.admin_list:
                    if admin.email == email and admin.get_password() == password:
                        is_admin_matched = True
                        current_admin = admin

                if is_admin_matched:
                    print('Admin matched')
                    print(f"WELCOME admin {admin.name} ({admin.admin_id}) ")

                elif is_admin_matched == False:
                    print("\tAdmin didn't match")

                if current_admin is not None:
                    while True:
                        print()
                        print('1. Show Admin Profile ')
                        print('2. See All Users ')
                        print('3. Delete Any User ')
                        print('4. Check the total balance of the bank ')
                        print('5. Check the total Loan amount of the bank ')
                        print('6. Loan Feature Control ')
                        print('7. Declaring Bankruptcy ')
                        print('8. Logout ')
                        print()

                        admin_opt = int(input('Enter admin option : '))

                        if admin_opt == 1:
                            # Show admin profile
                            current_admin.show_admin_profile()

                        elif admin_opt == 2:
                            # See all users
                            current_admin.see_all_users()

                        elif admin_opt == 3:
                            # Delete any user
                            print(f"Deleting an user account in progress ...")
                            account_id = input('Enter Account ID : ')
                            current_admin.delete_any_user(account_id)

                        elif admin_opt == 4:
                            # Check Balance of the bank
                            print(f"\tTotal Balance of the Bank : {dutch_bangla.get_available_balance()} tk ")

                        elif admin_opt == 5:
                            # Check Total Loan amount of the bank
                            print(f"\tTotal Loan Given : {dutch_bangla.get_given_loan()} tk ")

                        elif admin_opt == 6:
                            # Loan Feature control
                            dutch_bangla.is_loan_active = False
                            print(f"ADMIN has just turned off the loan feature of the bank. ")

                        elif admin_opt == 7:
                            # Declaring Bankruptcy
                            dutch_bangla.is_bankrupt = True
                            print(f"ADMIN has just declared Bankruptcy. ")

                        elif admin_opt == 8:
                            # Log out
                            print(f"Admin : {current_admin.name} Logged Out Successfully ")
                            current_admin = None
                            break

                        else:
                            print('Invalid Admin Option ')


            elif opt == 2:
                break

            else:
                print('Invalid Option chosen ')


    elif main_opt == 2:
        # Users part

        while True:
            print()
            print('1. Create User Account ')
            print('2. Log in User Account ')
            print('3. Exit ')
            print()
            ch = int(input('Enter choice : '))
            if ch == 1:
                # Creating an User account
                acc_type = input('Enter account type (s/c) ? : ')

                if acc_type.lower() == 's':
                    account_type = 'savings'
                    print()
                    print(f"Creating an Savings Account as User ... ")
                    name = input('Enter name : ')
                    email = input('Enter email : ')
                    password = input('Enter password : ')
                    address = input('Enter address : ')

                    Account.create_account(name, email, password, address, account_type)
                    print(f"\n{name}'s ({account_type}) account created successfully ")


                elif acc_type.lower() == 'c':
                    account_type = 'current'
                    print(f"Creating an Current Account as User ... ")
                    name = input('Enter name : ')
                    email = input('Enter email : ')
                    password = input('Enter password : ')
                    address = input('Enter address : ')

                    Account.create_account(name, email, password, address, account_type)
                    print(f"{name}'s ({account_type}) account created successfully ")

            elif ch == 2:
                # Logging in User Account
                print()
                print('Logging in as User ... ')
                email = input('Enter email : ')
                password = input('Enter password : ')
                print()

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

                        user_opt = int(input('Enter User Option : '))

                        if user_opt == 1:
                            # Deposit money
                            print('Deposit in progress ...')
                            d_amount = int(input('Enter amount : '))
                            if d_amount < 0:
                                print('Amount should be > 0 ')
                            elif d_amount > 0:
                                current_user.deposit_amount(d_amount)
                            # TODO: if user gives alphabets by mistake


                        elif user_opt == 2:
                            # Withdraw money
                            print(f"Bankrupt kina : {dutch_bangla.is_bankrupt}")
                            bankruptcy = dutch_bangla.is_bankrupt
                            print('Withdraw in progress ...')

                            w_amount = int(input('Enter amount : '))
                            current_user.withdraw_amount(w_amount, bankruptcy)


                        elif user_opt == 3:
                            # Check available balance
                            current_user.check_available_balance()



                        elif user_opt == 4:
                            # See Transaction history
                            print(f'--------- History of {current_user.name} ({current_user.acc_number}) ---------')
                            current_user.get_transaction_history()
                            print(f"----------------------------------------------")


                        elif user_opt == 5:
                            # Take Loan
                            # print(f"Loan Active kina : {dutch_bangla.is_loan_active}")
                            loan_active = dutch_bangla.is_loan_active
                            print('Taking Loan from bank ...')
                            loan_amount = int(input('Enter loan amount : '))
                            current_user.take_loan(current_user, loan_amount, loan_active)

                        elif user_opt == 6:
                            # Transfer money

                            '''
                                Receiver's account no. needs to be remembered 
                            '''
                            print('Money Transfer in progress ...')
                            print(f"Sender : {current_user.name} ({current_user.acc_number}) ")
                            sending_money = int(input('Enter amount to send : '))
                            current_user.transfer_money(sending_money, current_user)


                        elif user_opt == 7:
                            # Showing current loan amount
                            print(f"Current Loan : {current_user.get_loan_taken()} tk of {current_user.name}")

                        elif user_opt == 8:
                            # Logout
                            print(f"{current_user.name} ({current_user.acc_number}) Logged Out Successfully")
                            current_user = None
                            break


                        else:
                            print(f"Invalid Option ")
            elif ch == 3:
                break

            else:
                print('Invalid Option ')

    elif main_opt == 3:
        break

    else:
        print('Invalid Optin ! ')
