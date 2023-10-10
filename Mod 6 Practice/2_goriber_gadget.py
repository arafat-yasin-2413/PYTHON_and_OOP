class Gadget:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        print(f'Using {self.brand}')


class Laptop(Gadget):
    def __init__(self, brand, price, color, ssd):
        self.ssd = ssd
        super().__init__(brand, price, color)


class Phone(Gadget):
    def __init__(self, brand, price, color, dual_sim):
        super().__init__(brand, price, color)
        self.dual_sim = dual_sim


class Camera:
    def __init__(self, brand, price, color, pixel):
        super().__init__(brand, price, color)
        self.pixel = pixel


my_laptop = Laptop("Macbook", 1800, "Gray", "512 GB")
my_laptop.run()
print(my_laptop.brand, my_laptop.price, my_laptop.color, my_laptop.ssd)
print()

my_phone = Phone("Xiaomi", 300, "BLue", True)
my_phone.run()
print(my_phone.brand, my_phone.price, my_phone.color, my_phone.dual_sim)
print()
