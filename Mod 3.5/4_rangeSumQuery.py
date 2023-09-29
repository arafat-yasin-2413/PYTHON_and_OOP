n, q = map (int, input().split())

# print(n,q)

arr = list(map(int, input().split()))

# print(arr)
# print(type(arr[2]))

prefSum =[0] * n
prefSum[0] = arr[0]

for i in range(1,n):
    prefSum[i] = prefSum[i-1] + arr[i]

for i in range(q):
    L, R = map (int, input().split())
    L = L -1
    R = R -1

    if L == 0:
        print(prefSum[R])
    else:
        print(prefSum[R] -prefSum[L-1])