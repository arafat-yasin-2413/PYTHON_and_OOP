class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []



    def add_to_cart(self,item,price,quantity):
        product ={'item' : item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove_item(self,item):
        for product in self.cart:
            if item == product['item']:
                self.cart.remove(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            # print(item)
            total = total + item['price'] * item['quantity']

        print(f'You have to pay {total}')
        if amount < total:
            print(f'Please provide {total-amount} taka more')
        elif amount > total:
            print(f'Here is your change {amount-total} taka')
            print(f'Thank You For Shopping Sir')


moshiur = Shopping('Moshiur')
moshiur.add_to_cart('Alu',50,6)
moshiur.add_to_cart('Egg',12,24)
moshiur.add_to_cart('rice',50,5)

print(moshiur.cart)

print()

money_i_have = int(input('Enter your money : '))
moshiur.remove_item('Alu')
moshiur.checkout(money_i_have)