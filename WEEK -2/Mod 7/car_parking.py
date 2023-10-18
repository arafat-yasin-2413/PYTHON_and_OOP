


class Car:
    def __init__(self,licence):
        self.licence = licence
    def __repr__(self):
        return f"{self.licence}"


# class Parking_System:
#     def __init__(self,name,capacity):
#         self.name = name
#         self.parking_lot = Parking_Lot(capacity)


class Parking_Lot:
    def __init__(self,capacity):
        self.capacity = capacity
        self.available_slots = list(range(1,capacity+1))
        self.parked_cars = {}

    def park_my_car(self,car):
        if not self.available_slots:
            print('Slot khali nai')

        granted_slot = self.available_slots.pop(0)
        self.parked_cars[granted_slot] = car
        print(f"Car with licence {car.licence} successfully been parked")

    def leave_from_facility(self,granted_slot):
        if granted_slot in self.parked_cars.keys():
            leaving_car = self.parked_cars[granted_slot]
            print(f"Car with licence {leaving_car} Thank You. ")
            self.parked_cars.pop(granted_slot)
            self.available_slots.append(granted_slot)
            self.available_slots.sort()

        else:
            print(f'No car found at slot number {granted_slot}')

    def show_available_slots(self):
        print()
        print('------ Available Slots in our parking facility ------')
        print(self.available_slots)
        print()



    def check_available_slot(self):
        if not self.available_slots:
            return False
        else:
            return True





# main starts from here

parking_lot1 = Parking_Lot(10)

car1 = Car('Dhaka-123')
parking_lot1.park_my_car(car1)
parking_lot1.show_available_slots()



car2 = Car("Rajshahi-456")
parking_lot1.park_my_car(car2)
parking_lot1.show_available_slots()

car3 = Car("Dhaka-125")
parking_lot1.park_my_car(car3)
parking_lot1.show_available_slots()

car4 = Car("Dhaka-126")
parking_lot1.park_my_car(car4)
parking_lot1.show_available_slots()


car5 = Car("Dhaka-127")
parking_lot1.park_my_car(car5)
parking_lot1.show_available_slots()

car6 = Car("Dhaka-128")
parking_lot1.park_my_car(car6)
parking_lot1.show_available_slots()

car7 = Car("Dhaka-129")
parking_lot1.park_my_car(car7)
parking_lot1.show_available_slots()

car8 = Car("Dhaka-130")
parking_lot1.park_my_car(car8)
parking_lot1.show_available_slots()

car9 = Car("Dhaka-131")
parking_lot1.park_my_car(car9)
parking_lot1.show_available_slots()

car10 = Car("Dhaka-132")
parking_lot1.park_my_car(car10)
parking_lot1.show_available_slots()




#gari niye jacchi
parking_lot1.leave_from_facility(5)
parking_lot1.show_available_slots()

car11 = Car("Dhaka-133")
parking_lot1.park_my_car(car11)
