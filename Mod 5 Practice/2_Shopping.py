class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

        self.total = 0
        for things in self.cart:
            # print(things['item'])
            self.total += things['price'] * things['quantity']
        return self.total

    def checkout(self):
            return self.total

sakib = Shopping("Sakib Khan")
sakib.add_to_cart("Smartwatch",1000,4) # 4000
sakib.add_to_cart("Laptop",2000,2) # 4000
sakib.add_to_cart("Camera",5000,3) # 15000

print(sakib.checkout())
