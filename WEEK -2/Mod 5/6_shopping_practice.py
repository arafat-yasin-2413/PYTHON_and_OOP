class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
        # this cart is instance attribute

    def add_to_cart(self,item_name, price, quantity):
        # ekta product dictionary banabo
        product = {'item' : item_name, 'price': price, 'quantity':quantity}
        self.cart.append(product)

    isRemoved = False
    def remove_item(self,item_name):
        for things in self.cart:
            if things['item'] == item_name:
                self.isRemoved = True
                self.cart.remove(things)



    def checkOut(self,amount):
        total = 0
        for things in self.cart:
            total = total + (things['quantity'] * things['price'])
        print (f'Your Total Bill is : {total}')

        print(f'You Have Given {amount} tk')
        if amount < total:
            print(f'Sir, Please Provide {total-amount} tk More')
        else:
            if self.isRemoved:
                print(f"item removed successfully")
            print(f"Here's your products and Change {amount-total} tk")


moshiur = Shopping("Moshiuzzaman")
moshiur.add_to_cart('Alu',50,6)
moshiur.add_to_cart('Onion',70,5)
moshiur.add_to_cart('Chille',140,1)
moshiur.add_to_cart("Ice-Cream",1,50)
moshiur.remove_item('Ice-Cream')


print()
print(f'{moshiur.name} is purchasing : ')
print('******************************')


moshiur.checkOut(1000)
# for things in moshiur.cart:
    # print(f"{things['item']} -------- {things['quantity']} -------- {things['price']}")
