

n = int(input())

st = input()

list = []

for val in st.split():
    # list.append(val)
    list.append(int(val))

# print(type(list[0]))
# print(type(list[0]))

if list == list[::-1] : 
    print("YES")
else:
    print("NO")