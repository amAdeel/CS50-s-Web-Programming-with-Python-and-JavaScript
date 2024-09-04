
### SYNTAX of simple function 

def square(x):
    return x*x
for x in range(10):
    print(f"square of {x} is {square(x)}")




# Simple function
def greeting():
    print("helo world")
greeting()


# passing Argument and parameter
def date(name):
    print(f"My {name}")
date("Adeel")



#return statement 
def add(a,b):
    return a+b
add_result=add(5,3)
print(add_result)



#default parameter
def greeting1(name="world"):
    print(f"Hello,{name} !")
greeting1()
greeting1("Adeel Don")
# it's used when we can't define any parameter here then they automatically pik the default value  .


#There are many type of functions in python

#1 Build in function
numbers=[1,2,3,4,5]
print(sum(numbers))



#2 user-defined function : those function that we design according to our need
def helo(name):
    print(f"hello {name}")
helo("Adeel")



#3 
