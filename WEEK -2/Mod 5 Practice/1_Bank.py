class Bank:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} tk has been deposited Successfully")
            print(f"Total Balance after Depositing {amount} tk :{self.balance} tk")
        else:
            print(f'Invalid amount Given.Amount should be > 0')

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} tk withdraw successfull")
        else:
            print(f'Invalid amount.Try again!')
            print(f"Your Balance Status : {self.balance}")

    def check_balance(self):
        print(f"Your Current Balance is : {self.balance} tk")



my_account = Bank(10000)
my_account.check_balance()
my_account.withdraw(500)
my_account.check_balance()
my_account.deposit(5000)
my_account.deposit(233)