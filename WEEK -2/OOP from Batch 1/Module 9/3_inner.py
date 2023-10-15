'''

ekta function er vitore arekta function k declare korbo

'''

def do_something():
    print("Inside the do_something function")
    def inner_function():
        print("Inside the inner function")
    inner_function()


# do_something()


def first_function():
    print("Inside the first function")
    def second_function():
        print("Inside the inner function")
    return second_function

first = first_function()()
# first()

# print(first)
# print(type(first))