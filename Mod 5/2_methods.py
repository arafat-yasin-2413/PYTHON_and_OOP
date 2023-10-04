def call():
    print("Calling someone I don't know")
    return 'Call Done'





class Phone:
    # Setting some attribute
    # I mean declaring some variables
    price = 12000
    color = "blue"
    brand = "Samsung"
    features = ['Camera','Speaker','IR sensor']
    # ei boishishto gulo dynamic na

    def call(self):
        print('Calling one person')

    def sendSMS(self,phone,txt):
        text = f'Sending SMS to {phone} and message : {txt}'
        return text


my_phone = Phone()
# function er moto kore class k call korte hoy
# eikhane 'my_phone' hoilo ekta object


print(my_phone.features)
# print(my_phone.call())
my_phone.call()
msg = my_phone.sendSMS(33454,"How are you?")

print(msg)


'''
The code is showing 'None' in the output because the print(my_phone.call()) line is trying to print the return value of the call method, but the call method does not have an explicit return statement, so it implicitly returns None by default.

In Python, if a function or method doesn't have a return statement or if it reaches the end of the function without encountering a return statement, it returns None by default.

In your code, the call method is defined as follows:

python
Copy code
def call(self):
    print('Calling one person')
It prints the message 'Calling one person' but doesn't explicitly return any value. Therefore, when you call my_phone.call(), it prints the message and returns None, which is why you see 'None' in the output when you print the result of my_phone.call().

To avoid seeing 'None' in the output, you can simply call the call method without printing its return value like this:

python
Copy code
my_phone.call()
This will print 'Calling one person' without displaying 'None' in the output.

'''