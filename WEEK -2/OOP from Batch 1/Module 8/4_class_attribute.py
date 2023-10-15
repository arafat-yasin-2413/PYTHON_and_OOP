'''
Class attribute k sobai access korte pare. class attribute k 'static attribute' o bola hoy.
Class Attribute shared obosthay thake.
Amra jokhon kono variable ba attribute k sob instance er jonno same rakhte chai tokhon
class attribute byabohar kori.



'''

class Shop:
    cart = []
    def __init__(self,buyer):
        self.buyer = buyer


    def add_to_cart(self,item):
        self.cart.append(item)



moshiur = Shop("Moshiuzzaman")
moshiur.add_to_cart("Shirt")
moshiur.add_to_cart("Belt")
print(moshiur.cart)


print()

sajedul = Shop("Sajib")
sajedul.add_to_cart("Pant")
sajedul.add_to_cart("Shoes")
print(sajedul.cart)