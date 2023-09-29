def multiple():
    return 3, 4

# print(multiple())

things = 'pen','digital tab','digital pen','sci calc','neckband','smart band'

print(things[1])
print(things[-2])
print()

print(things[2:5])

print()

tpl = ([10,20,30],[40,50],'Sakib',[60,70,80,90])

tpl[0][1] = 99
# tpl[2] = 'Akib' # not possible doing this

print(tpl[0])
print(tpl[1])
print(tpl[2])
print(tpl[3])

print(len(tpl))