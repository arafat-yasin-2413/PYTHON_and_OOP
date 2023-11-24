class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


nokia_1 = Product('Nokia 1280', 3000, 10)
nokia_2 = Product('Nokia 1350', 2000, 7)
nokia_3 = Product('Nokia 1005', 1500, 6)
nokia_4 = Product('Nokia 1460', 1000, 12)



my_list = []
my_list.append(nokia_1)
my_list.append(nokia_2)
my_list.append(nokia_3)
my_list.append(nokia_4)

for item in my_list:
    print(f"{item.name}-- {item.price} tk --{item.quantity} unit")

