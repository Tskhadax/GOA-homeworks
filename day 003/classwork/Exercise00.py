##testing incredibly in your face

#error 0

print "hello"   #print("hello")
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?

#SyntaxError 1

x = 10                                     #x = 10
if x == 10                                 #if x == 10:

print("x is 10")                           #print("x is 10")

#SyntaxError: expected ':'

#NameError 2

def calculate_sum(a, b):                   #def calculate_sum(a, b):
total = a + b                              #total = a + b
return total                               #return total

x = 5                                      #x = 5
y = 10                                     #y = 10
z = calculate_sum(x, w)                    #z = calculate_sum(x, y)
print(z)                                   #print(z)

#NameError: name 'w' is not defined

#TypeError 3

x = "10"                       #x = "10"
y = 5                          #y = 5
Z = x + y                      #z = x + str(y)
print(z)                       #print(z)

#TypeError: can only concatenate str (not "int") to str

#IndexError 4

my_list = [100, 200, 300, 400, 500]        #my_list = [100, 200, 300, 400, 500]
print(my_list[5])                          #print(my_list[4])

#IndexError: list index out of range

#AttributeError

my_string = "Hello, world!"                #my_string = "Hello, world!"
my_string.reverse()                        #reversed_string = my_string[::-1]
print(reversed_string)                     #print(reversed_string)

#AttributeError: 'str' object has no attribute 'reverse'

#LogicalError 5

def calculate_factorial(n):                #def calculate_factorial(n):
    result = 1                             #    result = 1
    for i in range(1, n):                  #    for i in range(1, n+1):
          result = result * i              #         result = result * i
    return result                          #    return result

print(calculate_factorial(5))              #print(calculate_factorial(5))

#Output = 24                               #Output = 120

#2,000 errors for incredibly in your face emotes

#error code  / corected code

error -> stuff                             #eror = "stuff"
error -> stuff                             #eror = "stuff"
error -> stuff                             #eror = "stuff"
error -> stuff                             #eror = "stuff"
error -> stuff                             #eror = "stuff"
error -> stuff                             #eror = "stuff"
error -> stuff                             #eror = "stuff"
error -> stuff                             #eror = "stuff"
error -> stuff                             #eror = "stuff"