class Calculator():
    brand = "Casio MS-100MX"
    color = 'Black'

    def addition(self,num1,num2):
        add_res = num1+num2
        return add_res

    def subtraction(self,num1,num2):
        subt_res = num1-num2
        return subt_res

    def multiply(self,num1,num2):
        mult_res = num1 * num2
        return mult_res

    def divide(self,num1,num2):
        div_res = num1//num2
        return div_res

my_calculator = Calculator()
print(my_calculator.brand)

res1 = my_calculator.addition(10,15)
print(res1)

res2 = my_calculator.subtraction(30,12)
print(res2)

res3 = my_calculator.multiply(4,7)
print(res3)

res4 = my_calculator.divide(30,2)
print(res4)