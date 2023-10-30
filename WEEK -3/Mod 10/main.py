from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef, Customer,Server, Manager
from Order import Order
def main():
    menu = Menu()
    # add pizza to the menu
    pizza_1 = Pizza('Shutki Pizza',600,'large',['shutki','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('Alu Vorta Pizza',400,'large',['potato','onion','oil'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza('Dal Pizza',500,'large',['dal','oil'])
    menu.add_menu_item('pizza',pizza_3)

    # add burger to the menu
    burger_1 = Burger('Naga Burger',1000,'chicken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'Beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)

    # add drink to the menu
    coke = Drinks('Coke',50,True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('Mocha Coffee',300,False)
    menu.add_menu_item('drinks',coffee)

    # show menu
    # menu.show_menu()


    sai_baba = Restaurant('Sai Baba Restaurant',2000,menu)

    # add employees
    manager = Manager('Kala Chan Manager',5,'kala@chan.com','kalipur',1500,'Jan 1, 2020','core')
    sai_baba.add_employee('manager',manager)

    chef = Chef('Rustom Baburchi',6,'chuma@rustom.com','rustomnagar',3500,'Feb 1, 2020','Chef','everything')
    sai_baba.add_employee('chef',chef)

    server = Server('Chotu Roton',7,'nai@jai.com','restaurant',200,'Mar 1, 2020','server')
    sai_baba.add_employee('server',server)

    # show employees
    # sai_baba.show_employees()

    # customer_1 placing an order
    customer_1 = Customer('Sakib Khan',6,'king@khan.com','banani',100000)
    order_1 = Order(customer_1,[pizza_3,coke,burger_1,pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    sai_baba.add_order(order_1)
    # customer_1 paying for order_1
    sai_baba.receive_payment(order_1,4000,customer_1)
    print('revenue and balance after 1st customer',sai_baba.revenue, sai_baba.balance)


    # customer_2 placing an order
    customer_2 = Customer('Sakib Al Hasan',8,'sakib@al@hasan.com','Gulshan-2',500000)
    order_2 = Order(customer_2,[pizza_1,burger_2,burger_1,pizza_2, coffee])
    customer_2.pay_for_order(order_2)
    sai_baba.add_order(order_2)
    # customer_2 paying for order_2
    sai_baba.receive_payment(order_2,10000,customer_2)

    print('revenue and balance after 2nd customer',sai_baba.revenue, sai_baba.balance)

    # pay rent
    sai_baba.pay_expense(sai_baba.rent,'Rent')
    print('after paying rent',sai_baba.revenue, sai_baba.balance, sai_baba.expense)

    sai_baba.pay_salary(chef)
    print('after paying salary', sai_baba.revenue, sai_baba.balance, sai_baba.expense)











# calling the main
if __name__ == '__main__':
    main()