class Phone:
    brand = "Xiaomi"
    color = 'Blue'
    price = 25500

    def send_sms(self):
        print("sending sms...")

    def add(self,x,y):
        result= x + y
        return result
    def subtract(self,x,y):
        return x-y
    def mult(self,x,y):
        return x*y

my_phone = Phone()
print(my_phone)
print(my_phone.brand, my_phone.color, my_phone.price)
my_phone.send_sms()
print(my_phone.add(5,6))
print(my_phone.subtract(10,5))
print(my_phone.mult(6,7))