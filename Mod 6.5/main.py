'''

1. Create a Product class and a Shop class.

2. Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.

3. inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.



'''














class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Shop:
    def __init__(self):
        self.cart = []

    def add_product (self,name,price,quantity):
        product = {'name' : name, 'price':price,'quantity':quantity}
        self.cart.append(product)

    def buy_product(self,name,quantity):
        for things in self.cart:
            # print(things['quantity'])
            if name == things['name']:
                if quantity <= things['quantity']:
                    things['quantity'] -= quantity
                    return f'Congrats! You have successfully bought it'
                else:
                    return f"Sorry! {things['name']} is not available right now"
        return "Product not found in the shop."








my_shop = Shop()

my_shop.add_product("Laptop",1200,10)
my_shop.add_product("Phone",600,15)
my_shop.add_product("Tablet",900,8)



print(my_shop.buy_product("Laptop",2))
print(my_shop.cart)