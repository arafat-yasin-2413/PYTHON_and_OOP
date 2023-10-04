class Shop:
    shopping_mall = 'JFP'

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []
        # cart ta eikhane instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)


moshiur = Shop('Moshiur')
moshiur.add_to_cart('Shoes')
moshiur.add_to_cart('Phone')
print(moshiur.cart)

rakib = Shop('Rakib')
rakib.add_to_cart('Cap')
rakib.add_to_cart('Watch')
print(rakib.cart)