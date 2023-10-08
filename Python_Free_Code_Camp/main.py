# Polymorphism
# many forms -- vinno vinno roop

from phone import Phone
from keyboard import Keyboard

# item1 = Phone("iPhone12",1000,3)
item1 = Keyboard("A4TECH",1100,3)

item1.apply_discount()

print(item1.price)




















# Inheritance

# from phone import Phone
#
# item1 = Phone("iPhon12",1000,3)
#
# item1.apply_increment(0.2)
#
# print(item1.price)














# Abstraction
# from item import Item
#
# item1 = Item("MyItem",750)
#
# item1.send_email()
#
# item1.connect()















# Encapsulation
# from item import Item
#
# item1 = Item("MyItem",750)
#
# item1.apply_increment(0.2)
# item1.apply_discount()
#
# print(item1.price)
































# from item import Item
# # from phone import Phone
#
# # Item.instantiate_from_csv()
#
# item1 = Item("MyItem",750)
# item1.name = "OtherItem"
# print(item1.name)
# # print(item1.read_only_name)
#
# # item1.read_only_name = "BBB"
#
# # print(Item.all)
#
#
#


# Item.instantiate_from_csv()
#
# print(Item.all)

# print(Item.is_integer(7.0))


'''

print()
item1 = Item("Phone",100,1)
# print(f"Price after applying discount : {int(item1.apply_discount())} tk")
item1.apply_discount()
print(item1.price)

print()

item2= Item("Laptop",1000,3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)


'''

'''
item1 = Item("Phone",600,2)
# print(type(item1))
item2 = Item("Laptop",2800,3)


print(item1.calculate_total_price())
print(item2.calculate_total_price())

print()
print(Item.pay_rate) # accessing class attribute
print(item1.pay_rate)
print(item2.pay_rate)

print()
print("Priting attributes from levels")
print()

print(Item.__dict__) # accessing all class attributes
print()
print(item1.__dict__) # accessing instance attributes from item1
print()
print(item2.__dict__) # accessing instance attributes from item2

'''
