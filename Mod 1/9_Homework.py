# How folat Works
# fl = 5
# print(float(fl))


#  Take 3 numbers from the user and give me the largest number as output

# n1 = input('Enter a number : ')
# n2 = input('Enter a number : ')
# n3 = input('Enter a number : ')

# if n1 > n2 and n1 > n3:
#     print(f'Largest: {n1}')
# elif n2 > n1 and n2 > n3:
#     print(f'Largest: {n2}')
# else:
#     print(f'Largest: {n3}')



# Take 3 numbers as input and give the sum

# n1 = int(input('Enter a number : '))
# n2 = int(input('Enter a number : '))
# n3 = int(input('Enter a number : '))

# sum = n1+n2+n3

# print(f'Total Sum : {sum}')



# print odd numbers between 39 to 68

# for i in range(39,69):
#     if i%2 !=0:
#         print(i)


# Calculate grade with if, elif, else

marks = int(input('Enter your marks : '))

if marks >=33 and marks<=40:
    print(f'You have got D Grade')
elif marks>=41 and marks<=50:
    print(f'You have got C Grade')
elif marks>=51 and marks<=60:
    print(f'You have got B Grade')
elif marks >= 61 and marks<=70:
    print(f'You have got A- Grade')
elif marks>=71 and marks<=79:
    print(f'You have got A Grade')
elif marks>=80 and marks<=100:
    print(f'You have got A+ Grade')
elif marks <0 or marks>100:
    print(f'Invalid Marks')
else:
    print('Unfortunately, you are failed')