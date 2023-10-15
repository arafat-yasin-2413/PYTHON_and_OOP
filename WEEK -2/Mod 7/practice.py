class Vehicle:
    old = 3
    def __init__(self,name):
        self.name = name


car= Vehicle("BMW Sedan")
car.name = "Audi"
print(car.name)
Vehicle.old = 5
print(Vehicle.old)