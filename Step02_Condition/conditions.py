number=int(input("Enter your number: "))
if number>0:
    print('number is positive')
elif number<0:
    print('number is negative')
else:
    print('number is zero')    
#input methode always return a string then it's shows error , and the solution is that apply int () function over the input methode ehich convert the str value into int value.