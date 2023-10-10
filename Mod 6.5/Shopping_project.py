'''

1. Create a Product class and a Shop class.

2. Inside the Shop class, create a method name add_product which adds
products using the Product class to the Shop class.

3. inside the Shop class, create a method name buy_product which is used to buy a
product and check whether this product is available or not. If you successfully
buy a product, then throw a Congress message.



'''


class Product:
    def __init__(self, p_id, name, price, quantity):
        self.product_id = p_id
        self.name = name
        self.price = price
        self.quantity = quantity


class Shop:
    products = []

    def __init__(self, name):
        self.name = name

    def add_products(self, product):
        self.products.append(product)
        print(f"{product.name} added to {self.name}")

    def buy_product(self, p_id, wanted_quantity):
        for things in self.products:
            if things.product_id == p_id:
                if wanted_quantity <= things.quantity:
                    things.quantity -= wanted_quantity
                    print(f"{things.name} has been sold successfully")
                elif wanted_quantity > things.quantity:
                    print(f"This product : '{things.name}' is not available right now")



product1 = Product(1, "Laptop", 1200, 5)
product2 = Product(2, 'Phone', 300, 6)
product3 = Product(3, "Smartwatch", 50, 10)
product4 = Product(4, 'Neckband', 60, 8)

my_shop = Shop("My Gadget Store")

my_shop.add_products(product1)
my_shop.add_products(product2)
my_shop.add_products(product3)
my_shop.add_products(product4)
print()

moshiur = Shop("Moshiur")
moshiur.buy_product(2, 7)

print()
for thing in moshiur.products:
    print(f"{thing.name}, {thing.quantity}")


