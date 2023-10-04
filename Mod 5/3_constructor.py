class Phone:
    manufactured = "China"


    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price


    def send_sms(self,phone,txt):
        text = f'Sending to {phone} {txt}'
        # return text
        print(text)



my_phone = Phone('Jhankar','Oppo',9800)
print(my_phone.owner, my_phone.brand, my_phone.price)

his_phone = Phone("Sabbir",'iPhone',123000)
print(his_phone.owner, his_phone.brand,his_phone.price)

my_phone.send_sms(45367,"Hi there")
his_phone.send_sms(32345,'ki obostha')
print()

dad_phone = Phone('Baba','Nokia',3000)
print(dad_phone.owner, dad_phone.brand,dad_phone.price)