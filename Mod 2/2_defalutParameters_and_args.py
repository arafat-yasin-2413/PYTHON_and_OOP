
""" 
def sum(num1,num2,num3 = 0,num4 = 0, num5 = 0):
    result = num1 + num2 + num3
    return result

total = sum(35,36)
print(f'Total : {total}')


 """



def all_sum(num1,num2,*numbers):
    print(numbers)
    sum = 0
    for n in numbers:
        print(n)
        sum += n
    return sum
    
    

total = all_sum(45,10,34,54,34,15)
print(f'Total: {total}')