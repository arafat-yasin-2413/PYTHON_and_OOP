""" 
https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S
 """

""" 
কে কিসে আটকায় জানি না। কিন্তু আমি এইটাতে ইনপুট থেকে num1 আর num2 এক্সট্র্যাক্ট করতে আটকে গেছিলাম। পরে দেখি লিস্ট এর ইন্ডেক্স মেথড দিয়ে সুন্দরভাবে কাজ টা করা যায়। ব্যাপারটা একটু জোস । 
 """


test = int(input())
for test in range(test):
    # print(test)
    st = input()

    positionOfSpace= st.index(' ')
    a = int(st[:positionOfSpace])
    b = int(st[positionOfSpace+1:])

    # print(a)
    # print(b)

    sum = 0
    if a < b:
        for i in range(a+1,b):
            if i % 2 == 1:
                sum = sum + i

    if b < a:
        for j in range (b+1,a):
            if j % 2 == 1:
                sum = sum + j

    print(sum)









# """ 
# The error message you're seeing, ValueError: invalid literal for int() with base 10: '5 6', is occurring because you're trying to convert the string '5 6' into an integer using int(), but '5 6' is not a valid integer because it contains a space between the digits.

# If you have a string like '5 6' and you want to convert it into two separate integers, you'll first need to split the string into its individual parts and then convert each part to an integer. Here's an example of how you can do it:

#  """

# a = input()
# print()
# print (a[0])
# print (a[1])
# print (a[2])

# num1 = int(a[0])
# num2 = int(a[2])

# print()

# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))

# print()

# print(num1)
# print(num2)
# print()

# print(type(num1))
# print(type(num2))