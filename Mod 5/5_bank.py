class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance (self):
        return self.balance
        # print(f'Your current Balance is : {self.balance}')
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f'Total Balance after deposit : {self.balance}')

    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print(f'{self.min_withdraw} takar kom withdraw korte parbana')
        elif amount > self.max_withdraw:
            print(f'Bank Fokir hoye jabe. {self.max_withdraw} takar beshi withdraw korte parba na')
        elif amount > self.balance:
            print(f'Tomar to eto taka nai. Tomar ache matro {self.balance} taka')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            # print(f'Your current balance is : {self.balance}')
            print(f'Your Balance after withdrawing : {self.get_balance()}')

brac = Bank(15000)
curr_balance = brac.get_balance()
print(curr_balance)

brac.withdraw(14000)
brac.deposit(5000)


