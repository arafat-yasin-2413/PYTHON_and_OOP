
class Star_Cinema:
    __hall_list = []
    def entry_hall(self,obj):
        Star_Cinema.__hall_list.append(obj)

    @classmethod
    def print_hall_list(self):
        for things in Star_Cinema.__hall_list:
            print(things.rows, things.cols,things.hall_no)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self,iD,movie_name,tiMe):
        self.iD = iD
        self.movie_name = movie_name
        self.tiMe = tiMe
        make_tuple = (iD,movie_name,tiMe)
        self.show_list.append(make_tuple)

        self.seats[iD] = [ [0,0,0,0,0],
                           [0,0,0,0,0],
                           [0,0,0,0,0]
                        ]

        def book_seats(iD,lst):
            pass








object1 = Hall(3,5,2)
# Star_Cinema.print_hall_list()
object1.entry_show("MOVIE 1","Intersteller","11 am")
object1.entry_show("MOVIE 2",'The Shawshank Redemption','2 pm')
object1.entry_show("MOVIE 3",'Mission Impossible','5pm')
# print(object1.show_list)

# for movie in object1.show_list:
    # print (movie)


print(Star_Cinema.print_hall_list())

















