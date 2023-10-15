# public protected private

class Account:
    def __init__(self,holder):
        self._account_holder = holder

class StudentAccount(Account):
    def __init__(self,holder,balance,school):
        self.__balance = balance

    def withdraw(self,amount):
        if(amount > self.__balance):
            return 'No money for you'
        self.__balance -= amount
        return amount

    def deposit(self,amount):
        if amount < 0:
            return 'Negative amount can not be added'
        self.__balance += amount

    def get_balance(self):
        return self.__balance






sakib = StudentAccount("Sakib",12000,'IUB')
sakib.deposit(6000)
sakib.withdraw(5000)
print(sakib.get_balance())
# print(sakib._account_holder)

print(dir(sakib))
print(sakib._StudentAccount__balance)
