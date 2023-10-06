'''

def call():
    print("Calling someone I don't know")
    return 'Call Done'





class Phone:
    # Setting some attribute
    # I mean declaring some variables
    price = 12000
    color = "blue"
    brand = "Samsung"
    features = ['Camera','Speaker','IR sensor']
    # ei boishishto gulo dynamic na

    def call(self):
        print('Calling one person')

    def sendSMS(self,phone,txt):
        text = f'Sending SMS to {phone} and message : {txt}'
        return text


my_phone = Phone()
# function er moto kore class k call korte hoy
# eikhane 'my_phone' hoilo ekta object


print(my_phone.features)
# print(my_phone.call())
my_phone.call()
msg = my_phone.sendSMS(33454,"How are you?")

print(msg)

'''



class Phone:
    price = 34000
    brand = 'Samsung'
    color = 'Blue'

    def call(self):
        print(f'Calling someone I don\'t know')

    def send_sms(self,num,txt):
        print(f'Sending "{txt}" to {num}')




my_phone = Phone()
print(my_phone.brand)
print(my_phone.price)
print(my_phone.color)

my_phone.call()
my_phone.send_sms(8883455,"I Miss you")











