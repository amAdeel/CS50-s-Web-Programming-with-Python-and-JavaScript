#Recursion function is a function in which a function call itself in his own function

#Recursion function : have a base condition and a recursive call , if we can't provide a base condition then function can't stop itself and continous infinite time ... this base class is provided in if condition ,and then a recursive call start working 

def countdown(n):
    if n==0:
        print("Blast off")#Base call
    else:
        print(n)
        countdown(n-1)#recursive call

countdown(6)



#=========================> Find Factorial of a Number <==================================
# Now we discuss another example where we work on factorial : factorial is mathematical function 3!=3×2×1=6 like that now we done a function on it.

number=int(input("Find a Factorial (enter num) : "))# Alway remember input return a str value first convert it to int 
def factorial(number):
    if number==1:
        return 1
    else:
        return number * factorial (number-1)
    
print(factorial(number))


# in recursion function it's have a stack frame : what it's mean stack frame is like a note book like it's track and note down our last activity and it's work on LIFO methode mean last come first out .jab tak humari base nahi reach hoti os time tak humari stack chalti rehti hai or jab wo meat karti hai then we unwinding karny lag jata hai . like first time jab 5 ka factorial ly ga jo osy 4 ka factorial to chaye ho ga. " 5 * factorial 4 " , to wo is ko note down kar k (stack frame bana dy ga)or store kar ly ga , then wo "4 * factorial 3" pr jaye ga to new frame create ho ga or asy chaye k factorial 3 to ya asy bi wait karvy ga or new frame bana kar agy move kr jy ga .
# [factorial(5)]
# [factorial(4)]
# [factorial(3)]
# [factorial(2)]
# [factorial(1)]

# Or jab wo factorial 1 pR AYE  ga to 1 ka factorial which is 1 nikl ga is ko frame sy unwind kar dy ga or last wale ko remove kr dy ga .
#[factorial(5)]
# [factorial(4)]
# [factorial(3)]
# [factorial(2)]
# asi tara jasy osy baki factorial milty jy gy wo retuen karta jy ga or end pr answer return kary ga.








# Another example sum differnt number 


def add_up_to(n):
    if n == 0:
        return 0
    else:
        return n + add_up_to(n - 1)

print(add_up_to(5))

    


# Fibonacci sequence

#The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence typically starts with 0 and 1.

def fibonacci(n):
    if n<=1:
     return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) #first n-1 it's become 5 and 2nd n-2 it's become 3 and    5+3  it's return 8.
    
print(f"Fibonacci of a single number : {fibonacci(6)}")



# Now find a fibonacci series of multiplay number
def fibonacci1(n):
    if n<=1:
        return n
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
    
for i in range(10):
    print(f"{fibonacci1(i)}",end=" ") # here we use end=" " : what it's purpose we know when a print end new print comes in new line by defualt and by adding this me set our print where to go after " " , mean k adding space after each one .