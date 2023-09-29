st = input()


# string ta venge word alada kori
words = st.split()
# print(words)

# words ekhon ekta list 

# ekhon ekta ekta koira word niya reverse korbo
resultString=[]

for wrd in words:
    reversed_word = wrd[::-1]
    resultString.append(reversed_word)

for idx,char in enumerate(resultString):
    if idx == len(resultString)-1:
        print(char)
    else:
        print(char,end=' ')