class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.__password = password


class Customer(User):
    def __init__(self,name,email,password):
        super().__init__(name, email, password)


class Seller(User):
    def __init__(self,name,email,password):
        super().__init__(name, email, password)

    def publish_product(self):
        pass


class Create_Account(Customer,Seller):
    def __init__(self,name,email,password):
        super().__init__(name, email, password)





cust_1 = Create_Account('Mahmudullah Riyad','riyad@gmail.com','unlock_riyad')
seller_1 = Create_Account('Ghorerbazar_bd','ghorerbazarbd@gmail.com','unlock_gb')
print(seller_1.name, seller_1.email)
