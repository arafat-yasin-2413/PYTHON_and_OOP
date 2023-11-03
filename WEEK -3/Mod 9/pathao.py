class User:
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid

        self.wallet = 0


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        self.current_location = current_location
        super().__init__(name, email, nid)

    def accept_ride(self, ride):
        ride.set_driver(self)


class Rider(User):
    def __init__(self, name, email, nid, current_location, amount):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = amount
        self.current_ride = None

    def request_ride(self, ride_sharing, destination):
        if not self.current_ride:
            print('I am rider. looking for a ride.')
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            print('Got the ride', ride)
            self.current_ride = ride

    def show_current_ride(self):
        print(self.current_ride)


class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location

        self.driver = None
        self.rider = None

    def set_driver(self, driver):
        self.driver = driver

    def __repr__(self):
        return f"Ride Deatails. Started from : {self.start_location} to {self.end_location}"

class Ride_Request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class Ride_Matching:
    def __init__(self, list_of_driver_object):
        self.available_drivers = list_of_driver_object

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            print('looking for a driver')
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride


class Ride_Sharing:
    def __init__(self,company_name):
        self.company_name = company_name

        self.riders = []
        self.drivers = []
        self.rides = []


    def add_driver(self,driver):
        self.drivers.append(driver)

    def add_rider(self,rider):
        self.riders.append(rider)










pathao = Ride_Sharing('Pathao Ride Sharing Service')
sakib = Rider('Sakib Khan','sakib@gmail.com',456,'shyamoli',1000)
pathao.add_rider(sakib)
driver_1 = Driver('Roton Mia','roton@gmail.com',643,'shyamoli')
pathao.add_driver(driver_1)

sakib.request_ride(pathao,'Uttara')
sakib.show_current_ride()

# sakib.request_ride(pathao,'Mohakhali')
# sakib.show_current_ride()