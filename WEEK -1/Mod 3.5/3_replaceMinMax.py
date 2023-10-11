n = int (input())

str = input()

arr=[]
for val in str.split():
    arr.append(int(val))

# print(arr)
mx = max(arr)
mn = min(arr)

# print(mx,mn)

posOfmx = arr.index(mx)
posOfmn = arr.index(mn)
# print(posOfmx,posOfmn)

arr[posOfmx] = mn
arr[posOfmn] = mx

# print(arr)
for val in arr:
    print(val,end=' ')
