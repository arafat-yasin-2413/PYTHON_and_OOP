class Phone:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color
    def __repr__(self):
        return f"This is {self.brand} branded phone. Price is {self.price} tk and color is {self.color}"


my_phone = Phone("Apple",120000,'Purple')
# print(dir(my_phone))
# print(my_phone.__dict__)
print(my_phone)


