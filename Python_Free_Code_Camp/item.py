import csv


class Item:
    all = []
    pay_rate = 0.8

    def __init__(self, name, price, quantity=0):
        self.__name = name
        self.__price = price
        self.quantity = quantity

        self.all.append(self)
        # Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        # return self.__price

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value



    # this property name function getting the attribute@property
    @property
    def name(self):
        # print("You are trying to get name ")
        return self.__name

    @name.setter
    def name(self, value):
        # print("You are trying to set name ")
        if len(value)>10:
            raise Exception("The name is too long ")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name}, {self.__price}, {self.quantity}) "

    # @property
    # def read_only_name(self):
    #     return "AAA"

    def __connect(self,smtp_server):
        pass

    def __prepareBody(self):
        return f"""
        Hello Someone. 
        We have {self.name}
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepareBody()
        self.__send()


