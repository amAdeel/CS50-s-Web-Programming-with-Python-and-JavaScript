#==============================> Range <=================================================
####Range => A range is sequence of numbers , it's also has three kep point like a starting pointa ending point and a steping points . it normally used in loop conditions 
for i in range(5):
    print(i)


#example :
number=list(range(1,10,2))
print(number)#it's make number of list 

#example
# number1=[range(1,5)]
# print(number1)
#by applying above line it's only shows range(1,5)we run range proparly in a loop 
number1=[i**2 for i in range(1,11)]
print(number1)
