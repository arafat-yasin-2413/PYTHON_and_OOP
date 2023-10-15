'''

1. Create a Product class and a Shop class.

2. Inside the Shop class, create a method name add_product which adds
products using the Product class to the Shop class.

3. inside the Shop class, create a method name buy_product which is used to buy a
product and check whether this product is available or not. If you successfully
buy a product, then throw a Congress message.



'''


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




'''






























class Product:
    def __init__(self,item,price,quantity):
        self.item = item
        self.price = price
        self.quantity = quantity



class Shop:
    def __init__(self,name):
        self.name = name
    shop_cart = []
    def add_products(self,product):
        Shop.shop_cart.append(product)

    def buy_product(self,name,quantity):
        is_available = False
        has_bought = False
        for things in Shop.shop_cart:
            if name == things.item and quantity <= things.quantity:
                is_available = True
                if quantity <=things.quantity:
                    things.quantity -= quantity
                    has_bought = True
                    print(f"Congrats. You have bought {quantity} unit {name}")
        if is_available is not True or has_bought is not True:
            print(f"{name} is not available")











product1 = Product("Laptop",340000,15)
product2 = Product("Mobile",45000,20)
product3 = Product("Camera",60000,12)


my_shop = Shop("Goriber Gadget")
my_shop.add_products(product1)
my_shop.add_products(product2)
my_shop.add_products(product3)


my_shop.buy_product("Laptop",15)
my_shop.buy_product("Mobile",20)
my_shop.buy_product("Camera",12)
my_shop.buy_product("Mobile",2)


print()

for things in Shop.shop_cart:
    print(f"{things.item}, {things.price}, {things.quantity} unit")
