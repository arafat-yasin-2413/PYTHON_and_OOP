class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 1000
        self.max_withdraw = 100000

    def get_balance(self):
        return f"Current Balance = {self.balance} tk only"

    def deposit(self,amount):
        if amount < 0:
            print(f'Invalid amount is given. Provide amount > 0 ')
        elif amount == 0:
            print(f'{amount} taka deposit korte parbana tumi')
        else:
            self.balance += amount
            print(f"Deposit Done")
            return self.get_balance()

    def withdraw(self,amount):
        if amount < self.min_withdraw and amount > 0:
            print(f"{self.min_withdraw} takar kom tulte parbana")
        elif amount > self.max_withdraw:
            print(f"{self.max_withdraw} takar kom tulte parba")
        elif amount > self.balance:
            print(f"Tomar account a to eto taka nai. ")
            print(f"Tomar {self.get_balance()}")
        elif amount < 0:
            print(f"Shoytani baad diya nijer kaj koro jau")
            print(f"Tomar {self.get_balance()}")
        else:
            self.balance -= amount
            print(f"Money withdraw successfull")
            print(f"Here is your {amount} taka")
            return f"{amount} taka tolar por {self.get_balance()}"




my_bank = Bank(6000)
print(my_bank.get_balance())
# print(my_bank.deposit(500))
print(my_bank.withdraw(6000))
print(my_bank.deposit(13000))


