
class Restaurant:
    dishes = {}
    def __init__(self):
        pass


    def add_dishes_to_rest(self,name,price):
        Restaurant.dishes[name] = price

    def show_dishes(self):
        for item,price in Restaurant.dishes.items():
            print(f"{item} : {price}")


class Customer(Restaurant):
    def __init__(self):
        super().__init__()
        self.cart = []











# main starts from here
restaurant1 = Restaurant()
restaurant1.add_dishes_to_rest('Burger',60)
restaurant1.add_dishes_to_rest('Pizza',120)
restaurant1.add_dishes_to_rest('Pasta',80)

# restaurant1.show_dishes()
cust1 = Customer()
cust1.show_dishes()






