""" 
Careful: 
ইনপুট যদি 5 10 হয় , 

তাহলে, 
5^0 - 1 = 0
5^2 = 25
5^4 = 625
5^6 = ...
5^8 = ....
5^10= .....

মানে 5 এর পাওয়ার 10 পর্যন্ত হবার কথা। কিন্তু আমি লুপ 
চালাচ্ছিলাম for i in range(2,10,2)... 
এভাবে লুপ চালাইলে, i = 2,3,4,5,6,7,8,9 এর মধ্যে থেকে 
শুধু 2,4,6,8 কে নিবে। 10 কে তো পাবেই না। তাই লুপ টা 
i = 2 থেকে শুরু করে 1 বেশি পর্যন্ত চালাতে হবে যাতে করে 
2 থেকে 10 পর্যন্ত সবাইকে পায়। 



 """




st = input()
positionOfSpace = st.index(' ')
# print(positionOfSpace)

num1 = int(st[:positionOfSpace])
num2 = int(st[positionOfSpace+1:])

sum = 0
for i in range(2,num2+1,2):
    sum = sum + (num1 ** i)

print(sum)


