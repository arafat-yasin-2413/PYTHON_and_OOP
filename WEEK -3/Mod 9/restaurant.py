class Restaurant:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.rice_items = {}
        self.fish_items = {}
        self.meat_items = {}
        self.all_foods = {}

    def add_rice_items_to_inventory(self,obj):
        self.rice_items[obj.name] = obj
        self.all_foods[obj.name] = obj

    def add_fish_items_to_inventory(self,obj):
        self.fish_items[obj.name] = obj
        self.all_foods[obj.name] = obj

    def add_meat_item_to_inventory(self,obj):
        self.meat_items[obj.name] = obj
        self.all_foods[obj.name] = obj


    def show_rice_items(self):
        for key,value in self.rice_items.items():
            print(value)

    def show_fish_items(self):
        for key,value in self.fish_items.items():
            print(value)

    def show_meat_items(self):
        for key,value in self.meat_items.items():
            print(value)

    def show_all_foods(self):
        for key,value in self.all_foods.items():
            print(value)

class Food:
    def __init__(self, name,id, quantity, price):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.price = price


class Rice(Food):
    def __init__(self, name,id, quantity, price):
        self.rice_items = {}
        super().__init__(name,id, quantity, price)


    def __repr__(self):
        return f"Rice Item id: {self.id} - {self.name} - {self.quantity} -- Price: {self.price} tk"

class Fish(Food):
    def __init__(self, name,id, quantity, price):
        super().__init__(name,id, quantity, price)

    def __repr__(self):
        return f"Fish Item id: {self.id} - {self.name} - {self.quantity} -- Price: {self.price} tk"


class Meat(Food):
    def __init__(self, name,id, quantity, price):
        super().__init__(name,id, quantity, price)

    def __repr__(self):
        return f"Meat Item id: {self.id} , {self.name} - {self.quantity} -- Price: {self.price} tk"


class Customer:
    def __init__(self,name):
        self.name = name
        # bismillah.show_meat_items()
        self.price_list = []
        self.total_price = 0

    def show_foods(self,obj):
        obj.show_all_foods()

    def order_food(self,id,quantity):
        total = 0
        for key,value in bismillah.all_foods.items():
            if id == value.id:
                value.quantity -= quantity
                unit_price = value.price
                total += quantity * value.price
                self.price_list.append(total)
        print(f"{id}    {unit_price} *{quantity} unit = {total} taka")


    def show_total_bill(self):
        total = 0
        for items in self.price_list:
            total += items
        print()
        self.total_price = total
        print(f"You Have To Pay : {total} taka")

    def checkout(self,amount):
        if amount < self.total_price:
            print(f"Please provide {self.total_price - amount} taka more")
        else :
            if amount == self.total_price:
                print(f'You have paid {amount} taka. Thank You.')
            elif amount > self.total_price :
                print(f'You have paid {amount} taka.')
                print(f'Here is your change {amount - self.total_price} tk. Thank You.')

'''
can see food lists
can order foods

'''



# main starts from here

bismillah = Restaurant('Bismillah Restaurant','Ulail bazar,Savar')

# creating rice items
plain_rice = Rice('Plain Rice',111, 50, 20)
polau = Rice('Polau Premium', 112,40, 80)
khichuri = Rice('Khichuri', 113,30, 70)

# creating fish items
ilish1 = Fish('Ilish fry', 211, 40,60)
ilish2 = Fish('Mustard Ilish', 212, 60,120)
ilish3 = Fish('Ilish Curry', 213, 50,100)
rui1 = Fish('Rui vuna', 214, 70,120)
rui2 = Fish('Rui macher kalia', 215, 60,140)
rui3 = Fish('Rui curry', 216, 60,80)
pabda = Fish('Pabda Curry', 217, 50,90)
pangash = Fish('Pangash Vuna', 218, 40,80)

# creating meat items
deshi_murgi = Meat('Deshi Murgi Kosha', 311, 40,150)
beef = Meat('Beef Curry', 312,60,180)
mutton = Meat('Mutton Rejala', 313, 30,200)




bismillah.add_rice_items_to_inventory(plain_rice)
bismillah.add_rice_items_to_inventory(polau)
bismillah.add_rice_items_to_inventory(khichuri)
bismillah.add_fish_items_to_inventory(ilish1)
bismillah.add_fish_items_to_inventory(ilish2)
bismillah.add_fish_items_to_inventory(ilish3)
bismillah.add_fish_items_to_inventory(rui1)
bismillah.add_fish_items_to_inventory(rui2)
bismillah.add_fish_items_to_inventory(rui3)
bismillah.add_fish_items_to_inventory(pabda)
bismillah.add_fish_items_to_inventory(pangash)
bismillah.add_meat_item_to_inventory(deshi_murgi)
bismillah.add_meat_item_to_inventory(beef)
bismillah.add_meat_item_to_inventory(mutton)

# bismillah.show_rice_items()
# print()
# bismillah.show_fish_items()
# print()
# bismillah.show_meat_items()

print()
cust1 =Customer('Bulbul')
cust1.show_foods(bismillah)
print()
cust1.order_food(113,2)
cust1.order_food(212,3)
cust1.order_food(312,2)
cust1.show_total_bill()
cust1.checkout(1000)

print()

cust2 = Customer('Robin')
cust2.show_foods(bismillah)