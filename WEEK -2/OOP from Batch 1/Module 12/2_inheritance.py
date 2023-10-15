class Vehicle:
    def __init__(self,name,license,price):
        self.name = name
        self.license = license
        self.price = price

    def start(self):
        print(f"{self.name} has started")



class Bus(Vehicle):
    def __init__(self,name,license,price,seat,ticket_price):
        self.seat = seat
        self.available_seat = seat
        self.ticket_price = ticket_price
        print("Bus init called")
        super().__init__(name,license,price)

    def sell_ticket(self,customer_name, quantity,ticket_price,amount):
        self.available_seat -= quantity
        remaining = amount - (self.ticket_price * quantity)
        if remaining >= 0:
            return Ticket(customer_name)
        return f'no ticket for you'


class ACBus(Bus):
    def __init__(self):
        print("AC bus created")

class Minibus(Bus):
    def __init__(self):
        print("This is minibus created")
        super().__init__("City Minibus Service","DH1234",120000,18,450)

class Ticket:
    def __init__(self,owner ):
        self.owner = owner


mini_bus = Minibus()
print(mini_bus.seat)
print(mini_bus.name)