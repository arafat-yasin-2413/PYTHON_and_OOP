class Father:
    def __init__(self):
        self.__balance =6000


    def get_balance(self):
        return self.__balance

class Child(Father):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def get_balance2(self):
        print(self._Father__balance)


father_obj = Father()
# print(father_obj.get_balance())
child_obj = Child('Alex')
child_obj.get_balance2()