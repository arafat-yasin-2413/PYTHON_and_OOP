def full_name(first,last):
    name = f'full name is : {first} {last}'
    return name


# nm = full_name('Alu',"Kodu")
nm = full_name(last = 'Kodu',first= 'Alu')
# print(nm)



# def famous_name(first,last,title,addition):
#     name = f'{title} {first} {last}'
#     return name

# nm = famous_name('Abu','Naser','Chowdhury','Khan')
# print(nm)




# def famous_name(first,last,**addition):
#     name = f'{first} {last}'
#     # print(addition['title'])
#     for key, value in addition.items():
#         print(key, value)
#     return name

# nm = famous_name(first= 'Siraj',last='Uddoula',title='Nobab',title2='Monsur',last2='Ul muluk')
# print(nm)



def ops(num1,num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    return sum,mult,remain

everything = ops(12,4)
print(everything)
     