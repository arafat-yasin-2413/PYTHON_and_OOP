'''class Phone:
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

'''








class Phone:
    def __init__(self,a,b,c,d):
        self.owner = a
        self.brand = b
        self.price = c
        self.color = d

    def call(self,x):
        self.number = x
        print(f'Calling {x}')

    def send_SMS(self,x,y):
        self.number = x
        self.txt = y
        print(f'Sending text message : {self.txt} to {self.number}' )




my_phone = Phone("Akash",'iPhone',120000,'Purple')
print(my_phone.owner, my_phone.brand, my_phone.price, my_phone.color)
my_phone.call(786434)
my_phone.send_SMS(8116,'Happy Birthday dear')












