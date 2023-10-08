from item import Item


class Phone(Item):
    # all = []

    def __init__(self, name, price, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        self.broken_phones = broken_phones

        # Phone.all.append(self)


phone1 = Phone("iPhone10", 500, 5, 1)
# print(phone1.calculate_total_price())
phone2 = Phone("iPhone11", 700, 5, 1)

# print(Item.all)
# print(Phone.all)
