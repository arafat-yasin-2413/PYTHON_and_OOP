"""
map ছাড়া pythen এ একই লাইন এ দুই বা ততোধিক ইনপুট নিব কিভাবে?


David Kudrot
just use,
variabl_name = input().split()
it will return a list



Mahmud Pias
Moderator
Top contributor
  · 
এক লাইনে দুটি ইন্টিজার ইনপুট এভাবে নিতে পারেন।
a,b = input().split()
a = int(a)
b = int(b)



a, b = [int(x) for x in input().split()]




Split use kora hoy ek line e onek gula input thakle....
Apnr ta hobe tik amon....
N,Q=int(input().split()) (apni split diye dui like e input nicen tai error dekhaice split diye ek line er sob gula input dewa hoy) Ekhane ektar moddhe array size(N)+taste case(Q) dui tai paben....etar jonno muloto apnke error dekhaice....
"""