# Difference between class attributes and instance attributes

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
