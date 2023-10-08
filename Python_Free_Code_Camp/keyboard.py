from item import Item


class Keyboard(Item):

    pay_rate = 0.6 #beauty of inheritance and polymorphism in one line. Because overriding a class attribute is legal
    def __init__(self,name,price,quantity=0):
        super().__init__(name,price,quantity)