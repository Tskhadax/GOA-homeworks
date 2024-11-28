# 2)  შექმენით პროგრამა რომელიც დაითვლის სიაში რამდენჯერ მეორდება თქვენი სახელი არ გამოიყენოთ count ფუნქცია 

my_list = ["sopia", "sopia", "lazare", "sopia", "tea"]

my_name = input("enter your name: ")

c = 0

 
for elements in my_list:
    if elements == my_name:
        c += 1
print(c)
