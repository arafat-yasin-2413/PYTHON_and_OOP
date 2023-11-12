'''
1. Customers can CREATE A/C , SEE PRODUCTS, PLACE ORDER
2. Sellers can CREATE A/C, CREATE PRODUCT, PUBLISH PRODUCTS
3. MONITOR THE STOCK AFTER PLACING AN ORDER

'''

class E_Shopping:
    def __init__(self,name):
        self.name = name

        self.customers = []
        self.sellers = []
        self.inventory = []

        self.revenue = 0
        self.total = 0
        self.orders = []

    def add_customer_to_the_system(self,customer_object):
        self.customers.append(customer_object)

    def add_sellers_to_the_system(self,seller_object):
        self.sellers.append(seller_object)

    def show_sellers(self):
        print(f"_________________Our Sellers_________________")
        for seller in self.sellers:
            seller.show_profile()


    def show_customers(self):
        print(f"_________________Our Customers_________________")
        for customer in self.customers:
            customer.show_profile()

    



    def add_products_to_the_inventory(self,product_object):
        self.inventory.append(product_object)


    def show_all_product(self):
        print(f'*************** Welcome to {self.name} ***************')
        print(f"***************OUR AVAILABLE PRODUCTS***************")
        print()
        for gadget in self.inventory:
            if gadget.quantity !=0:
                gadget.info()
        print(f'------------------------------------------------------')

    def receive_order(self,cust_obj,ordered_items):
        pass

    def calculate_bill(self,cust_obj,ordered_items):
        total = 0
        for item in ordered_items:
            # print(item.name, item.price,'tk')

            if item.quantity == 0:
                print(f"{item.name} is stock out")
                break
            elif item.quantity >= 1:
                total += item.price
        self.total = total
        print(f'Your total bill is {self.total} tk')

    def receive_payment(self,cust_obj,amount):
        if amount > self.total:
            self.revenue += self.total
            print(f'Thank you {cust_obj.name} for shopping')
            print(f'Here is your change {amount-self.total} tk')

        elif amount < self.total:
            print(f'Please provide {self.total - amount} tk more')
    
    def verify_seller(self,email,password):
        for seller in self.sellers:
            if email == seller.email and password == seller.get_password:
                return seller


    def verify_customer(self,email,password):
        for customer in self.customers:
            if email == customer.email and password == customer.get_password:
                return customer
