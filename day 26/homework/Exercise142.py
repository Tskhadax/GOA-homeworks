# 6) შექმენით სია რომელშიც იქნება სახელები შემდეგ კი შექმენით პროგრამა რომელიც ამოშლის ყველა სახელს რომელიც "t" ასოზე იწყება და ჩაამატებს ახალ სიაში

my_list = ["sopia", "sopia", "lazare", "sopia", "tea", "tako"]
t_names = []

for elements in my_list:
    if elements[0] == "t":
        t_names.append(elements)



print(t_names)