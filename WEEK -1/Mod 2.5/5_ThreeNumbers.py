# K, S = map(int, input().split())
# count = 0

# for x in range(K + 1):
#     for y in range(K + 1):
#         z = S - x - y
#         if 0 <= z <= K:
#             count += 1

# print(count)


st = input()
positionOfSpace = st.index(' ')

K = int(st[:positionOfSpace])
S = int(st[positionOfSpace+1:])

cnt = 0
for i in range(K + 1):
    for j in range(K+1):
        sum = S - i - j
        if sum >= 0 and sum <=K:
            cnt = cnt+1

print(cnt)