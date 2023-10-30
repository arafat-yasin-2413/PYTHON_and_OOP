class Pharmacy:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.inventory ={}

    def add_to_inventory(self,obj):
        self.inventory[obj.name] = obj

    def show_inventory(self):
        for key,value in self.inventory.items():
            print(value)

class Medicine:
    def __init__(self,name,manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        self.inventory = {}



# 1st level inheritance starts
class Tablet(Medicine):
    def __init__(self,name, manufacturer, tablet_quantity):
        super().__init__(name, manufacturer)
        self.tablet_quantity = tablet_quantity
    def __repr__(self):
        return f"{self.name} : {self.manufacturer} : {self.tablet_quantity}"

class Capsule(Medicine):
    def __init__(self, name, manufacturer, capsule_quantity):
        super().__init__(name, manufacturer)
        self.capsule_quantity = capsule_quantity
    def __repr__(self):
        return f"{self.name} : {self.manufacturer} : {self.capsule_quantity}"
class Syrup(Medicine):
    def __init__(self, name, manufacturer, syrup_quantity):
        super().__init__(name, manufacturer)
        self.syrup_quantity = syrup_quantity

    def __repr__(self):
        return f"{self.name} : {self.manufacturer} : {self.syrup_quantity}"
# 1st level inheritance ends



# 2nd level inheritance starts
# Derived classes of Tablet Class starts
class Gastric_Tablet(Tablet):
    pass

class Fever_Tablet(Tablet):
    pass

class Pain_Tablet(Tablet):
    pass

# Derived classes of Tablet Class Ends



# Derived classes of Capsule Class Starts
class Antibiotic_Capsule(Capsule):
    pass

class Calcium_Capsule(Capsule):
    pass

class Gastric_Capsule(Capsule):
    pass

class Vitamin_Capsule(Capsule):
    pass
# Derived classes of Capsule Class Ends


# Derived classes of Syrup Class Starts
class Vitamin_Syrup(Syrup):
    pass

class Syrups_for_Childs(Syrup):
    pass

class Cough_Syrup(Syrup):
    pass
# Derived classes of Syrup Class Ends
# 2nd level inheritance ends






# main starts from here
bonik = Pharmacy('Bonik Pharmacy','Thana Road, Savar')

aceclofenac=Tablet("Aceclofenac bp 20mg",'Renata Pharma',100)
dexlan = Capsule("Dexlan 500mg",'Incepta Pharma',50)
tuska = Syrup('Tuska 100ml','Labaid Pharma',20)



bonik.add_to_inventory(aceclofenac)
bonik.add_to_inventory(dexlan)
bonik.add_to_inventory(tuska)

bonik.show_inventory()
