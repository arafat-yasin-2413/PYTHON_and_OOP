""" 
https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y

 """

""" 
Errors I digested:

1.
The error message you're encountering, "IndexError: list assignment index out of range," suggests that you're trying to assign a value to an index in a list that doesn't exist yet. This typically happens when you try to assign a value to an index that is greater than or equal to the current length of the list.

In the context of your code, it seems like you are attempting to assign a value to fibo[0], but fibo is either an empty list or has not been defined yet. To fix this issue, you need to create a list and then assign values to its elements. Here's an example of how to create a list to store Fibonacci numbers and initialize the first element to 0:



2.
It seems like you're encountering an issue where you're getting the string representation of a function object instead of the expected result. This typically happens when you try to print or use a function without actually calling it.

If you see <function function_name at memory_address>, it means you are referring to the function itself without calling it.
 """




num = int (input())
fibo=[0,1]

for i in range(2,num):
    fibo.append(fibo[i-1] + fibo[i-2])

for val in fibo[:num]:  #শুধু [:num] 
    print(val,end=' ')


# [:num] এইটা লিখলে ইনপুট যদি 1 দিই তাহলে আউটপুট শুধু ১ টা ইলিমেন্টের জন্য দেখানোর কথা। আর এভাবে না লিখলে ইনপুট 1 এর জন্য আউটপুটে 0 1 দেখাচ্ছিলো। 
