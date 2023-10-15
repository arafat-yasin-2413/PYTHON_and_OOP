import random

class User:
    def __init__(self,f_name,l_name):
        self.first = f_name
        self.last = l_name
        self.email = f"{f_name.lower()}.{l_name.lower()}{random.randint(1,1000)}@gmail.com"

    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    @property
    def get_email(self):
        return f"{self.email}"



rakib = User("Rakib",'Hossain')
# print(rakib.first)
# print(rakib.last)
# print(rakib.email)
# print(rakib.full_name)
# print(rakib.get_email)
rakib.first = "Tom"
print(rakib.full_name)
rakib.full_name = "Tom Hanks"