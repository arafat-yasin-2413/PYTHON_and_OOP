'''class Bank:
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

'''









class Bank:
    min_withdraw = 100
    max_withdraw = 1000000
    min_deposit = 1000
    def __init__(self,balance):
        self.balance = balance
        if self.balance < 1000:
            print(f'Minimum {self.min_deposit} taka deposit korte hobe')

    def get_balance(self):
        print(f'Current Balance : {self.balance}')

    def deposit(self,amount):
        if amount > 0 and amount >= 1000:
            self.balance += amount
            print(f'Current Balance after deposit : {self.balance}')



    def withdraw(self,amount):
        if self.balance < amount:
            print(f'Tumi agee deposit koro')

        elif self.balance >= amount:
            if amount<self.min_withdraw:
                print(f'Eto kom taka tulte parbana. {self.min_withdraw} takar beshi tulte hobe.')
            elif amount > self.max_withdraw:
                print(f'Bank deulia hoye jabe.{self.max_withdraw} er kom tulte parba')
            else:
                self.balance -= amount
                print(f'Here is your {amount} taka.')
                print(f'Your current balance after withdraw {self.balance}')








brac = Bank(1600)
brac.get_balance()

brac.withdraw(100)











