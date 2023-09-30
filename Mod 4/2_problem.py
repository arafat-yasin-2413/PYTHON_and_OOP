""" একটা অ্যারে দেওয়া থাকবে সেখানে যে এলিমেন্ট গুলা থাকবে ওই এলিমেন্ট এর কাউন্ট টা ওই এলিমেন্ট এর সমান হতে হবে..
যেমন;
১ ২ ২ ৩
এখন এই অ্যারে তে ১ এক বার থাকতে হবে, সেটা আছে
এরপর ২ কে ২ বার থাকতে হবে সেটাও ঠিক আছে
কিন্তু ৩ কে ৩ বার থাকতে হবে কিন্তু এক বার আছে..
তাই এখন এই অ্যারে কে আমরা যদি good সিকোয়েন্স বানাতে চাই তাইলে ৩ এর কাউন্ট কে রিমুভ করতে হবে..
সো ans হবে ১
আর যদি এমন হতো
১ ৩ ৩ ৩ ৩ ৩
৩ কে ৩ বার থাকার কথা ছিল কিন্তু ৫ বার আছে তাই ৫-৩ অর্থাৎ ২ টা ৩ কে বাদ দিবো
সো ans ২
এক্ষেত্রে আপনি ফ্রিকোয়েন্সি অ্যারে বা ডিকশনারি এর হেল্প নিতে পারেন.. """


n = int(input())
lst = list(map(int, input().split()))

# print(lst)
# print(type(lst))

# dictionary nilam
counter = {}


for val in lst:
    if val in counter:
        counter[val] += 1 
    else:
        counter[val] = 1

# for idx, x in counter.items():
#     print(f'{idx} : {x}')

to_remove = 0
ans = 0
for idx, x in counter.items():
    # print(idx,x)

    # occurence jodi value er soman hoy , taile kichui korbo na
    if idx == x:
        ans = ans + to_remove
    # occurence kom hoile sei occurence ta baad dibo
    if x < idx:
        ans = ans + x
    # karo occurence beshi hoile tar count theke value baad diye baki kaj
    else:
        ans = ans + (x-idx)

print(ans)
