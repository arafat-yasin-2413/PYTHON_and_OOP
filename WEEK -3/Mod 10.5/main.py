from abc import ABC,abstractmethod
from User import  Customer, Seller
from Product import Phone,Laptop,Neckband,Ram
from E_Shopping import E_Shopping
def main():
    daraz = E_Shopping("Daraz Online")

    



    # daraz.show_all_product()
    # print()
    # daraz.show_sellers()
    # print()
    # daraz.show_customers()
    # print(f'___________________________________________________')
    # print()


    while(True):
        print('Option 1 : Create Account')
        print('Option 2 : Login')
        print('Option 3 : Add Products to the inventory')
        print('Option 4 : Show all Products')
        print('Option 5 : Add to order')
        print('Option 6 : Show ordered items')
        print('Option 7 : Calculate bills')
        print('Option 8 : Make Payment')
        print('Option 9 : Exit')
        print()

        choice = int(input('Enter option: '))
        if choice == 1:
            user_type = input('As Seller/Customer (S/C): ')
            if user_type.lower() == 's':
                print(f'Creating Seller account')
                name = input('Enter name : ')
                email = input('Enter email : ')
                password = input('Enter password : ')
                seller_obj = Seller(name,email,password)
                daraz.add_sellers_to_the_system(seller_obj)

            elif user_type.lower() == 'c':
                print(f'Creating Customer Account')
                name = input('Enter name : ')
                email = input('Enter email : ')
                password = input('Enter password : ')
                cust_obj = Customer(name,email,password)
                daraz.add_customer_to_the_system(cust_obj)
                

        elif choice == 2:
            user_type = input('Log in as Seller/Customer (S/C): ')
            if user_type.lower() == 's':
                email = input('Enter email to login : ')
                password = input('Enter password to login : ')
                current_seller = daraz.verify_seller(email,password)
                # current_seller.show_profile()
                # can add products
                # can publish products
            elif user_type.lower() == 'c':
                email = input('Enter email to login : ')
                password = input('Enter password to login : ')
                current_cust = daraz.verify_customer(email,password)
                # current_cust.show_profile()



        elif choice == 3:
            print("Let's create some products")
            type = input('Enter type of the product : ')
            times = int(input('How many model : '))
            for i in range(times):
                p_name = input('Enter name of the product : ')
                p_price = input('Enter price : ')
                p_quantity = int(input('Enter quantitiy: '))
                if type.lower() == 'phone':
                    phone_obj = Phone(p_name,p_price,p_quantity)
                    daraz.add_products_to_the_inventory(phone_obj)
                elif type.lower() == 'laptop':
                    laptop_obj = Laptop(p_name,p_price,p_quantity)
                    daraz.add_products_to_the_inventory(laptop_obj)
            
        elif choice == 4:
            daraz.show_all_product()

        elif choice == 5:
            # current_cust.show_profile()
            print(f'{current_cust.name} is shopping')
            while(True):
                print(f'option-1 : Add to order')
                print(f'option-2 : See All Products')
                print(f'option-3 : Quit adding')

                ch = int(input('Enter your choice'))
                if ch == 1:
                    prod_name = input('Enter product name : ')
                    current_cust.add_to_order(prod_name)
                elif ch == 2:
                    daraz.show_all_product()

                elif ch == 3:
                    break

            
        elif choice == 6:
            # show ordered items
            for item in range(len(current_cust.ordered_items)):
                for product in daraz.inventory:
                    if product.name == item:
                        product.info()
            
        elif choice == 7:
            # calculate bills
            total = 0
            for item in range(len(current_cust.ordered_items)):
                for product in daraz.inventory:
                    if product.name == item:
                        if product.quantity >= 1:
                            total += product.price
            print(f"{current_cust.name} Sir/Madam, Your total bill is {total} tk")
        elif choice == 8:
            # make payment
            amount = input('Enter amount to pay : ')
            daraz.receive_payment(current_cust,amount)
        elif choice == 9:
            break









if __name__ == '__main__':
    main()