class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Employee:
    def __init__(self, name, joining_date, salary_per_day, employee_type):
        self.name = name
        self.joining_date = joining_date
        self.salary_per_day = salary_per_day
        self.employee_type = employee_type

    def __repr__(self):
        return f"{self.employee_type.lower()} : name : {self.name}, joined on : {self.joining_date} "


class Manager(Employee):
    def __init__(self, name, joining_date, salary_per_day, employee_type):
        super().__init__(name, joining_date, salary_per_day, employee_type)
        self.joining_date = joining_date
        self.salary_per_day = salary_per_day
        self.employee_type = employee_type
        self.due_salary = salary_per_day
        self.wallet = 0



    def pay_salary(self, employee_type):
        pass

    def __repr__(self):
        return Employee.__repr__(self)


class Chef(Employee):
    def __init__(self, name, joining_date, salary_per_day, employee_type):
        super().__init__(name, joining_date, salary_per_day, employee_type)
        self.salary_per_day = salary_per_day
        self.employee_type = employee_type
        self.due_salary = salary_per_day
        self.wallet = 0


    def __repr__(self):
        return Employee.__repr__(self)


class Server(Employee):
    def __init__(self, name, joining_date, salary_per_day, employee_type):
        super().__init__(name, joining_date, salary_per_day, employee_type)
        self.salary_per_day = salary_per_day
        self.employee_type = employee_type
        self.due_salary = salary_per_day
        self.wallet = 0

    def __repr__(self):
        return Employee.__repr__(self)


class Food_Items:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}  -->  {self.price} tk"


class Burger(Food_Items):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients

    def __repr__(self):
        return Food_Items.__repr__(self)


class Pizza(Food_Items):
    def __init__(self, name, price, size, ingredients):
        super().__init__(name, price)
        self.size = size
        self.ingredients = ingredients

    def __repr__(self):
        if self.size == 'regular':
            return f"{self.name} (R) --> {self.price} tk"
        elif self.size == 'medium':
            return f"{self.name} (M) --> {self.price} tk"
        elif self.size == 'large':
            return f"{self.name} (L) --> {self.price} tk"

class Restaurant:
    def __init__(self, restr_name):
        self.restr_name = restr_name

        self.rent = 3000

        self.burgers = []
        self.pizzas = []
        self.all_foods = []

        self.manager = []
        self.chefs = []
        self.servers = []

        self.payable = 0

        self.revenue = 0
        self.balance = 0
        self.expense = 0
        self.profit = 0

    def add_foods_to_restaurant(self,food_type,food):
        if food_type.lower() == 'burger':
            self.burgers.append(food)

        elif food_type.lower() == 'pizza':
            self.pizzas.append(food)
        self.all_foods.append(food)

    def add_employees(self, employee_type, employee):
        if employee_type.lower() == 'manager':
            self.manager.append(employee)
        elif employee_type.lower() == 'chef':
            self.chefs.append(employee)
        elif employee_type.lower() == 'server':
            self.servers.append(employee)

    def show_employees(self):
        print(self.manager)
        print(self.chefs)
        print(self.servers)

    def show_all_food_items(self):
        print('---------------- Our Tasty Items ----------------')
        for food in self.all_foods:
            print(food)

    def total_payable_for_customer(self,payable):
        self.payable = payable
        print(f'Please Pay : {payable} tk')

    def collect_bill_from_customer(self,amount):
        if amount > self.payable:
            self.revenue += self.payable
            self.balance += self.payable
            print(f'Here is your change {amount-self.payable} tk')

        elif amount < self.payable:
            print(f'Please provide {self.payable - amount} tk more')


    def pay_rent(self):
        print()
        print(f"Rent {self.rent} tk Paid Successfully")
        self.balance -= self.rent
        self.expense += self.rent


    def pay_salary(self,employee_type,employee):
        if employee_type.lower() == 'manager':
            if self.balance < employee.salary_per_day:
                print(f'No Salary Today {employee_type}. Ask Tomorrow with day counts.')
            elif self.balance > employee.salary_per_day:
                employee.wallet += employee.salary_per_day
                employee.due_salary -= employee.salary_per_day
                self.balance -= employee.salary_per_day
                self.expense += employee.salary_per_day

        elif employee_type.lower() == 'chef':
            if self.balance < employee.salary_per_day:
                print(f'No Salary Today {employee_type}. Ask Tomorrow with day counts.')
            elif self.balance > employee.salary_per_day:
                employee.wallet += employee.salary_per_day
                employee.due_salary -= employee.salary_per_day
                self.balance -= employee.salary_per_day
                self.expense += employee.salary_per_day

        elif employee_type.lower() == 'server':
            if self.balance < employee.salary_per_day:
                print(f'No Salary Today {employee_type}. Ask Tomorrow with day counts.')
            elif self.balance > employee.salary_per_day:
                employee.wallet += employee.salary_per_day
                employee.due_salary -= employee.salary_per_day
                self.balance -= employee.salary_per_day
                self.expense += employee.salary_per_day

    def calculate_restaurant_profit(self):
        self.profit = self.revenue - self.expense


    def show_revenue(self):
        print()
        print('$$$$$$$$$$ REVENUE $$$$$$$$$$')
        print(f"Total Revenue : {self.revenue} tk")

    def show_balance(self):
        print()
        print('$$$$$$$$$$ BALANCE $$$$$$$$$$')
        print(f"Current Balance : {self.balance} tk")

    def show_expense(self):
        print()
        print('$$$$$$$$$$ EXPENSE $$$$$$$$$$')
        print(f"Total Expense : {self.expense} tk")

    def show_profit(self):
        print()
        print('$$$$$$$$$$ PROFIT $$$$$$$$$$')
        print(f"Total Profit : {self.profit} tk")


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.ordered_items = []

    def __repr__(self):
        return f"Customer with name {self.name} , and email : {self.email}"

    def add_to_order(self,item):
        self.ordered_items.append(item)

    def calculate_bill(self):
        total = 0
        for item in self.ordered_items:
            total += item.price
        print()
        print(f'\t\tHello *{self.name}* Sir/Madam ! ')
        print(f"Your total bill is : {total}")
        bismillah.total_payable_for_customer(total)




    def pay_bill(self,amount):
        bismillah.collect_bill_from_customer(amount)










bismillah = Restaurant('Bismillah Restaurant')
manager1 = Manager('Moin Akhter', '10 Sept 2022', 3500, 'Manager')
# print(manager1)

chef1 = Chef('Rafsan Hoque', '14 Mar 2021', 2000, 'chef')
# print(chef1)
chef2 = Chef('Sonny Side', '14 May 2021', 2000, 'chef')

server1 = Server('Sabbir', '18 Jan 2023', 400, 'server')
# print(server1)


bismillah.add_employees('manager', manager1)
bismillah.add_employees('chef', chef1)
bismillah.add_employees('chef', chef2)
bismillah.add_employees('server', server1)
# bismillah.show_employees()

burger_1 = Burger('Chicken Burger', 240, ['chicken', 'lettuce', 'sauce'])
burger_2 = Burger('Beef Burger', 390, ['beef', 'onions', 'pickles', 'mayo'])
burger_3 = Burger('Premium Burger', 760, ['3 patty', 'naga morich', 'chille sauce'])
pizza_1 = Pizza('Chicken Pizza', 360, 'regular', ['Chicken', 'garlic sauce'])
pizza_2 = Pizza('Kima Pizza', 890, 'medium', ['beef kima', '3 sauce item', 'drink'])
pizza_3 = Pizza('Tandoori Pizza', 1520, 'large', ['Tanduri beef', 'cheese'])


bismillah.add_foods_to_restaurant('burger',burger_1)
bismillah.add_foods_to_restaurant('burger',burger_2)
bismillah.add_foods_to_restaurant('burger',burger_3)
bismillah.add_foods_to_restaurant('pizza',pizza_1)
bismillah.add_foods_to_restaurant('pizza',pizza_2)
bismillah.add_foods_to_restaurant('pizza',pizza_3)

bismillah.show_all_food_items()
print()

cust_1 = Customer('Sakib Khan','sakib@gmail.com','Savar')
cust_1.add_to_order(burger_3)
cust_1.add_to_order(pizza_3)
cust_1.add_to_order(pizza_3)
cust_1.add_to_order(burger_1)
cust_1.add_to_order(burger_2)
cust_1.add_to_order(burger_3)
cust_1.add_to_order(pizza_3)
cust_1.add_to_order(pizza_3)
cust_1.calculate_bill()
cust_1.pay_bill(10000)



cust_2 = Customer('Nayeem Khan','nayeem@gmail.com','Gazipur')
cust_2.add_to_order(pizza_2)
cust_2.add_to_order(burger_2)
cust_2.add_to_order(burger_1)
cust_2.add_to_order(pizza_2)
cust_2.add_to_order(burger_2)
cust_2.add_to_order(burger_1)
cust_2.add_to_order(pizza_3)
cust_2.add_to_order(burger_3)
cust_2.add_to_order(pizza_3)
cust_2.add_to_order(pizza_3)
cust_2.calculate_bill()
cust_2.pay_bill(15000)



bismillah.show_revenue()
bismillah.pay_rent()
bismillah.show_balance()


bismillah.pay_salary('Manager',manager1)
bismillah.pay_salary('Chef',chef1)
bismillah.pay_salary('Chef',chef2)
bismillah.pay_salary('server',server1)
bismillah.calculate_restaurant_profit()

bismillah.show_revenue()
bismillah.show_expense()
bismillah.show_profit()
bismillah.show_balance()


