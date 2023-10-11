balance = 3000

def buy_something(item,price):
    global balance
    balance = balance - price
    print(f'Balance after buying : {item}, {balance}')


buy_something('sunglass',1000)
