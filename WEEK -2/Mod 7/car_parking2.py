class Parking_Lot:
    def __init__(self,capacity):
        self.capacity = capacity
        self.available_slots = list(range(1,capacity+1))
        self.parked_cars = {}

    def park_my_car(self,car):
        if not self.available_slots:
            print(f'Slot khali nai')
        else:
            granted_slot = self.available_slots[0]
            self.available_slots.pop(0)
            self.parked_cars[granted_slot] = car
            print(f'Car with licence {car.licence} successfully Parked')


    def leave_parking_lot(self,reserved_slot):
        if reserved_slot not in self.parked_cars.keys():
            print(f'No Car Has Found at slot {reserved_slot}')

        elif reserved_slot in self.parked_cars.keys():
            slot = reserved_slot
            leaving_car = self.parked_cars[reserved_slot]
            self.parked_cars.pop(slot)
            self.available_slots.append(slot)
            print(f"Car {leaving_car} is leaving. Thank You. ")


    def show_available_slots(self):
        self.available_slots.sort()
        print(self.available_slots)


class Car:
    def __init__(self,licence):
        self.licence = licence

    def __repr__(self):
        return f'{self.licence}'




car1 = Car('DM-111')
car2 = Car('DM-112')
car3 = Car('DM-113')
car4 = Car('DM-114')
car5 = Car('DM-115')
car6 = Car('DM-116')

# print(car1.licence)

parking_lot1 = Parking_Lot(5)

parking_lot1.show_available_slots()
parking_lot1.park_my_car(car1)
parking_lot1.show_available_slots()

parking_lot1.park_my_car(car2)
parking_lot1.show_available_slots()

parking_lot1.park_my_car(car3)
parking_lot1.show_available_slots()

# parking_lot1.park_my_car(car4)
# parking_lot1.show_available_slots()
#
# parking_lot1.park_my_car(car5)
# parking_lot1.show_available_slots()

# parking_lot1.park_my_car(car6)
# parking_lot1.show_available_slots()

# parking_lot1.leave_parking_lot(6)
# parking_lot1.show_available_slots()

parking_lot1.park_my_car(car6)
parking_lot1.show_available_slots()

parking_lot1.leave_parking_lot(40)
parking_lot1.show_available_slots()