#1) შექმინთ 2 სია  , პირველი სია ინქება ცარიელი  ხოლო მეროე სია ინქება სახელებით სავსე მინიმუმ 5 , თქვენი დავალებაა ამ სიიდან  ჩაამოტომ მეორე სიაში სახელელბი რომელიც  4 სიმბოლოზე ნაკლებია
names = ["rezi", "mate", "gio", "mari", "toko",]

names2 = []
 
for i in names:
    if len(i) < 4:
        names2.append(i)
print(names2)