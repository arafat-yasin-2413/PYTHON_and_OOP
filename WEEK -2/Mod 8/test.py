my_list = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
my_dict ={}
my_dict['122'] = my_list

#
# key = '122'
# if key in my_dict:
#     list_2 = my_dict[key]
#     list_2[1][2] = 5



matrx = my_dict['122']
for row in matrx:
    for element in row:
        print(element)
        break






