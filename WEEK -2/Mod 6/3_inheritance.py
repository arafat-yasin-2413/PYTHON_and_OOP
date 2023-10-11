# base class, parent class
# common attribute + functionality class

# derived class, child class
# Uncommon attribute + functionality



class Gadget:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running Laptop : {self.brand}'

class Laptop:
    def __init__(self,memory,ssd):
        self.memory = memory
        self.ssd = ssd


    def coding(self):
        return f'Learning Python'


class Phone(Gadget):
    def __init__(self,brand,price,color,origin,dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)

    def phone_call(self, number, text):
        return f'Sending SMS to {number} with : {text}'

    def __repr__(self):
        return f' Phone:: {self.brand} {self.price} {self.color} {self.origin} {self.dual_sim}'


class Camera:
    def __init__(self,pixel):

        self.pixel = pixel

    def change_lense(self):
        pass




# inheritance
my_phone = Phone('iPhone',12000,'Purple','USA',True)

# print(my_phone.phone_call(777958116,'Your anger wins'))

# print(my_phone.brand)
# print(my_phone.dual_sim)

print(my_phone)