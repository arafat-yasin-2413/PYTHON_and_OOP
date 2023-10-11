""" Romjan Ali
Moderator
Top contributor

Max Split
এখানে আপনাকে একটা স্ট্রিং দেওয়া থাকবে সেখান থেকে কয়টা ব্যালেন্স স্ট্রিং বানানো যাবে সেটা বলতে হবে। ব্যালান্স স্ট্রিং হচ্ছে যেখানে L এবং R এর সংখ্যা সমান থাকবে
Good Sequence
এখানে একটা গুড সিকুয়েন্স হচ্ছে যেখানে এরের প্রতিটা ইলেমেন্ট তার মানের সংখ্যক বার আছে যেমন ইলেমেন্ট যদি ১ হয় তাহলে এরেতে এটা শুধু ১ বার এ থাকবে যদি ২ হয় তাহলে ২ এরেতে ২ বার থাকবে এইভাবে প্রতিটা ইলেমেন্ট এর জন্য চেক করতে হবে এখন আপনাকে বলতে হবে মিনিমাম কয়টা ইলেমেন্ট রিমুভ করলে এরেটাকে Good Sequence বানানো সম্ভব """


st = input()
# print(st)

L = 0
R = 0
cnt = 0

# print(type(L))
# print(type(R))

temp=""
# print(type(temp))
lst=[]
# print(type(list))

for idx, char in enumerate(st):
    # print(idx,char)
    if char == 'L':
        L =L+1
        temp = temp + char
    else:
        R =R+1
        temp = temp+char
    
    if L == R:
        lst.append(temp)
        cnt = cnt + 1
        temp = ""


# print(cnt)
print(len(lst))

# print(lst)
for string_s in lst:
    print(string_s)