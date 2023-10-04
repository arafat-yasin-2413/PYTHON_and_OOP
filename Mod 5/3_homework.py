class Pen:
    manufactured = "Bangladesh"

    def __init__(self,brand,ink_color,price):
        self.brand = brand
        self.ink_color = ink_color
        self.price = price



my_pen = Pen('Matador','Black',7)
his_pen = Pen('Linc','Red',15)
her_pen = Pen('Econo DX','Green',20)

print(my_pen.brand, my_pen.ink_color, my_pen.price)
print(his_pen.brand, his_pen.ink_color, his_pen.price)
print(her_pen.brand, her_pen.ink_color, her_pen.price)
