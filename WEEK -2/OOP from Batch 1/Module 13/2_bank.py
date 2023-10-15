# Encapsulation
class Account:
    def __init__(self,holder,initial_balance):
        self.holder = holder
        self._account_number = 165
        self.__balance = initial_balance
    def deposit(self,amount):
        print(f"Adding {amount} tk to your account")
        self.__balance += amount

    def withdraw(self,amount):
        print(f"Withdrawing {amount} tk from your account")
        self.__balance -= amount

class StudentAccount(Account):
    def __init__(self,holder,initail_balance,school):
        self.school = school
        super().__init__(holder,initail_balance)

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self._account_number

rafsan = StudentAccount("Rafsan",50000,"IUB")
# print(rafsan.balance)
rafsan.deposit(20000)
rafsan.deposit(35000)
rafsan.deposit(15000)
# rafsan.__balance = 0
# print(rafsan.__balance)

# print(rafsan.get_balance())
rafsan._account_number = 125
print(rafsan.get_account_number())