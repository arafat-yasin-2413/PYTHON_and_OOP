""" https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q """




""" 
Corner case : ইনপুট zero হলে কি করবেন সেটা হ্যান্ডেল করতে ভুলে যায়েন না। 

 """


test = int(input())
for i in range(0,test):
    num = int(input())
    if num == 0:
        print(0)
    else:
        while num != 0:
            print(num % 10,end=' ')
            num = num // 10
        print()
        # print(1234//10)