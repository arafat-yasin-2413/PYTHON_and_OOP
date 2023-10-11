n = int(input())
lst = list(map(int, input().split()))

requiredOps =0
while True:
    is_even = True

    for val in lst:
        if val % 2 != 0:
            is_even = False
            break
    
    if is_even == True:
        for i in range(n):
            lst[i] = lst[i]//2
        requiredOps += 1

    else:
        break


print(requiredOps)    







