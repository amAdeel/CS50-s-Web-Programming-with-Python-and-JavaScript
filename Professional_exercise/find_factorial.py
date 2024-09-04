# Find Factorial of following number enter your number , here we using recursive function 


number=int(input("Find Factorial (enter-num) : "))
def factorial(number):
    if number ==1:  # Act as as base call
        return 1
    else:
        return number * factorial(number-1) # Act As a recursive call
    
print(factorial(number))