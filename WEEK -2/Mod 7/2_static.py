class Shopping:
    cart = [] # This cart is a class attribute
    # ei class attribute k 'static attribute ' o bola hoy

    def __init__(self,name,location):
        self.name = name
        self.location = location
        # here, name and location both are
        # ...instance attrtibute

    def purchase(self,item,price,amount):
        self.item = item
        self.price = price
        self.amount = amount

        remaining = amount - price
        print(f'Buying {item} for {price} tk and remaining : {remaining}')

    @classmethod
    def hudai_dekhi(self,item):
        print('AC er batash khaite aschi',item)

#     static method
    @staticmethod
    def multiply(a,b):
        print(a*b)



my_cart = Shopping('JFP',"Panthapath")
# my_cart.purchase("Egg",12,300)
my_cart.hudai_dekhi("Shirts")
Shopping.hudai_dekhi("Pants")
my_cart.multiply(4,5)
Shopping.multiply(3,4)