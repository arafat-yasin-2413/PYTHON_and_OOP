class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"PRODUCT_NAME: {self.name}; PRICE: {self.price}tk; AVAILABLE_UNIT: {self.quantity}"



class Phone(Product):
    def __init__(self,name,price,quantity,specs_list):
        super().__init__(name, price, quantity)
        self.specs_list= specs_list

    def show_specifications(self):
        print(f'Showing specs for {self.name}')
        print(self.specs_list)

    def __repr__(self):
        return Product.__repr__(self)



class Laptop(Product):
    def __init__(self, name, price, quantity, specs_list):
        super().__init__(name, price, quantity)
        self.specs_list = specs_list

    def show_specifications(self):
        print(f'Showing specs for {self.name}')
        print(self.specs_list)

    def __repr__(self):
        return Product.__repr__(self)


class Smartwatch(Product):
    def __init__(self, name, price, quantity, specs_list):
        super().__init__(name, price, quantity)
        self.specs_list = specs_list

    def show_specifications(self):
        print(f'Showing specs for {self.name}')
        print(self.specs_list)

    def __repr__(self):
        return Product.__repr__(self)


class Neckband(Product):
    def __init__(self, name, price, quantity, specs_list):
        super().__init__(name, price, quantity)
        self.specs_list = specs_list

    def show_specifications(self):
        print(f'Showing specs for {self.name}')
        print(self.specs_list)

    def __repr__(self):
        return Product.__repr__(self)




iphone_12 = Phone('Iphone 13',140000,10,['12 MP Rear', '12 MP Front','4/128 storage'])
iphone_14 = Phone('Iphone 14 Pro',180000,15,['48 MP Rear', '12 MP Front','4/256 storage'])

print(iphone_12)
print(iphone_14)
iphone_12.show_specifications()
iphone_14.show_specifications()