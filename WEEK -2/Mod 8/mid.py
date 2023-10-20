class Star_Cinema:
    __hall_list = []

    def entry_hall(self,obj):
        Star_Cinema.__hall_list.append(obj)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        super().__init__()
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self,id,movie_name,time):
        my_tuple = (id,movie_name,time)
        # print(type(my_tuple[0]))
        self.show_list.append(my_tuple)
        my_list = [ [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]
                ]
        self.seats[id] = my_list

        # print(self.seats.keys())


    def book_seats(self,id_of_the_show,seat_list):
        is_invalid_seat = False
        for row,col in seat_list:
            # print(row,col)
            if row < 0 or col >= 5:
                is_invalid_seat = True
                print('Invalid seat is given')

        if is_invalid_seat == False:
            if id_of_the_show in self.seats:
                for item in seat_list:
                    row = item[0]
                    col = item[1]

                    if self.seats[id_of_the_show][row][col] == 1:
                        print(f"This seat {(row,col)} is already booked. Enter correct row, columns.")
                    elif self.seats[id_of_the_show][row][col] == 0:
                        self.seats[id_of_the_show][row][col] = 1
                print(f"Seat booked successfully")




    def view_show_list(self):
        print('-------------------------------------')
        print(f"\t\t'Running Shows'")
        for things in self.show_list:
            print(things)
        print('-------------------------------------')

    def view_available_seats(self,id):
        seat_matrix = self.seats[id]
        print(f'Available Seats for show : {id}')
        for row in seat_matrix:
            for element in row:
                print(element, end=' ')
            print()




cinema_hall = Hall(5,5,1)
cinema_hall.entry_show('122',f'Intersteller','11 am')
cinema_hall.entry_show('123','13 Hours','2 pm')
cinema_hall.entry_show('124','Perfume','5 pm')

# cinema_hall.get_available_seats('122')
# seatList = [(1,2),(1,3),(2,0)]
# cinema_hall.book_seats('122',seatList)
# cinema_hall.view_available_seats('122')
# cinema_hall.view_show_list()
# cinema_hall.view_available_seats('123')



# options to be created
'''
1. counter can view all shows running
2. counter can view available seats in a show
3. can book tickets in a show

'''

print("\t\tWelcome to 'cinema hall'\n")
print("This is counter")
print('1. View all shows running')
print('2. View available seats in a show')
print('3. Book your ticket')
print('4. Exit Console\n')



while True:

    option = int(input('Enter option : '))

    if option == 1:
        cinema_hall.view_show_list()

    elif option == 2:
        movie_id = input('Enter movie id : ')
        is_movie_found = False

        i = len (cinema_hall.show_list)
        # print(i)

        for j in range(i):
            # print('for loop a dhuksi')
            # print(cinema_hall.show_list[0][0])
            if movie_id == cinema_hall.show_list[j][0]:
                # print('if condition a dhuksi')
                is_movie_found = True

        if is_movie_found:
            # print('movie found condition a dhuksi')
            cinema_hall.view_available_seats(movie_id)
            # is_movie_found = False
        else:
            # print('last else a dhuksi')
            print('Invalid Movie id is given')

    elif option == 3:
        iD = input('Enter movie id : ')
        i = len(cinema_hall.show_list)
        # print(i)
        is_id_matched = False
        for j in range(i):
            if iD == cinema_hall.show_list[j][0]:
                number_of_seats = int(input('How many seats you need : '))
                my_list = []
                for i in range(number_of_seats):
                    print(f'Enter row, col for {i + 1}-th seat')
                    row = int(input())
                    col = int(input())
                    my_tuple = (row, col)
                    my_list.append(my_tuple)
                print(my_list)
                cinema_hall.book_seats(iD, my_list)
                is_id_matched = True

        if is_id_matched == False:
            print('Invalid movie id is given. Please provide correct movie id. ')


    elif option == 4:
        break

    print("This is counter")
    print('1. View all shows running')
    print('2. View available seats in a show')
    print('3. Book your ticket')
    print('4. Exit Console\n')


