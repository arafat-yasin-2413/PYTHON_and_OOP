class Shopping:
    def __init__(self,cust_name):
        self.cart = []
        self.customer_name = cust_name

    def welcome(self):
        print()
        print(f'****** Welcome to EASY FASHION LTD. ******')
        print(f"Welcome Mr./Mrs. {self.customer_name}. Thank you for coming.")


    def add_to_cart(self,item,price,quantity):

        product = {'item_name': item, 'price': price, 'quantity': quantity}
        # product is a dictionary
        self.cart.append(product)


    def checkout(self,amount):
        total = 0
        print()
        print(f'Your items are :')
        print('------------------')
        for things in self.cart:
            # print(things)

            print(things['item_name'], things['price'], things['quantity'])
            total += things['price'] * things['quantity']
        print()
        print(f'Sir/Madam your total bill is : {total} tk')
        print(f'You have paid                : {amount} tk')

        if amount < total:
            print(f"Please Provide '{total-amount}' tk more. ")

        elif amount == total:
            print(f"Here is your items. Thank You For Shopping With Us. Please Come Again. ")

        else:
            # the given amount is higher than the total bill
            print(f"Here is your change          : {amount-total} taka")
            print(f"And here is your items. Thank You and Please Come Again.")
        # print(type(things))


moshiur = Shopping("Moshiuzzaman")
moshiur.welcome()
moshiur.add_to_cart("Shirt",800,3)
moshiur.add_to_cart("Pant",2500,2)
moshiur.add_to_cart("Sandal",540,6)
moshiur.checkout(11000)