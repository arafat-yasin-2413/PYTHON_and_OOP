# Function is a first class object in python

def double_decker():
    print('Starting the double decker')
    def inner_func():
        print('Inside the inner')
        return 3999
    return inner_func

# print(double_decker())
# print(double_decker()())


def do_something(work):
    print('Work Started')
    # print(work)
    work()
    print('Work Ended')


# do_something("ami busy")

def writing():
    print('thinking in python')

# do_something(writing)


def sleeping():
    print('Sleeping and dreaming in python')

do_something(sleeping)