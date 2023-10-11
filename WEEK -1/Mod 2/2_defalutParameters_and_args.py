
""" 
def sum(num1,num2,num3 = 0,num4 = 0, num5 = 0):
    result = num1 + num2 + num3
    return result

total = sum(35,36)
print(f'Total : {total}')


 """



def all_sum(num1=0,num2=0,*numbers):
    print(f'num1 = {num1}')
    print(f'num2 = {num2}')
 
    print(numbers)
    sum = 0
    for n in numbers:
        print(n)
        sum += n
    return sum
    
    

total = all_sum(10,20,30,40,50)
print(f'Total: {total}')