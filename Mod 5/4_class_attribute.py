# Difference between class attributes and instance attributes

"""
class Shop:
    cart = []
    # cart ta eikhane class attribute
    def __init__(self,buyer):
        self.buyer = buyer

    def addtocart(self,item):
        self.cart.append(item)

Moshiur = Shop('Moshiuzzaman')
Moshiur.addtocart('Shoes')
Moshiur.addtocart('Phone')
print(Moshiur.cart)


Rakib = Shop('Rakib')
Rakib.addtocart('Cap')
Rakib.addtocart('Watch')
print(Rakib.cart)
"""


class Shopping:
    cart = []
    def add_to_cart(self,item):
        self.cart.append(item)




akash = Shopping()
akash.add_to_cart('Cap')
akash.add_to_cart('Shoes')
akash.add_to_cart('Belt')
print(f'Cart of Akash : {akash.cart}')

batashi = Shopping()
batashi.add_to_cart('Lipistick')
batashi.add_to_cart('Nail Polish')
batashi.add_to_cart('Orna')
print(f'Cart of Batashi: {batashi.cart}')





















