'''
class attribute gulo k sorasori class er naam diye ebong object er naam diye access kora jay.
kintu instance attribute gulo k class er naam diye sorasori access kora jay na.
Istance attribute gulo k access korar jonno instacne name er por dot diye sei
attribute er naam likhe access korte hoy. 


'''


class Phone:
    manufactured = "China"
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color



my_phone = Phone("Samsung",30000,'White')
her_phone = Phone("iPhone", 120000,"Purple")


print(my_phone.brand, my_phone.price, my_phone.color,my_phone.manufactured)
print(her_phone.brand, her_phone.price, her_phone.color, her_phone.manufactured)
print(my_phone.manufactured)
print(her_phone.manufactured)