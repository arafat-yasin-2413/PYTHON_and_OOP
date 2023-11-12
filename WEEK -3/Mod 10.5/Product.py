from abc import ABC,abstractmethod
class Product(ABC):
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def info(self):
        raise NotImplementedError

class Phone(Product):
    def __init__(self,name,price,quantity):
        super().__init__(name, price, quantity)
        # self.specs = specs

    def info(self):
        print(f'Name: {self.name}, Price: {self.price} tk , Available: {self.quantity} unit')



class Laptop(Product):
    def __init__(self,name,price,quantity):
        super().__init__(name, price, quantity)
        # self.specs = specs

    def info(self):
        print(f'Name: {self.name}, Price: {self.price} tk , Available: {self.quantity} unit')



class Neckband(Product):
    def __init__(self,name,price,quantity):
        super().__init__(name, price, quantity)
        # self.specs = specs

    def info(self):
        print(f'Name: {self.name}, Price: {self.price} tk , Available: {self.quantity} unit')


class Ram(Product):
    def __init__(self,name,price,quantity):
        super().__init__(name, price, quantity)
        # self.specs = specs

    def info(self):
        print(f'Name: {self.name}, Price: {self.price} tk , Available: {self.quantity} unit')
