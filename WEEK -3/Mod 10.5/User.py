from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.__password = password

    @abstractmethod
    def show_profile(self):
        raise NotImplementedError

    @property
    def get_password(self):
        return self._User__password  
    




class Customer(User):
    def __init__(self,name,email,password):
        super().__init__(name, email, password)
        self.ordered_items = []
        self.total = 0

    @property
    def get_password(self):
        return self._User__password   
    

    def show_profile(self):
        print(f"Customer's name: {self.name}, email: {self.email}")


    def add_to_order(self,product_name):
        self.ordered_items.append(product_name)


        



class Seller(User):
    def __init__(self,name,email,password):
        super().__init__(name, email, password)

    @property
    def get_password(self):
        return self._User__password  
    

    def show_profile(self):
        print(f"Seller's name: {self.name}, email: {self.email}")


# seller_1 = Seller('Roton Mia','roton@gmail.com',3456)
# # print(seller_1._User__password)
# print(seller_1.get_password)

