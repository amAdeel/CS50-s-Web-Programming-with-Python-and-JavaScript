## For Loops 
#syntAX
for i in [1,2,3,4,5]:
    print(i)

# Here another way if i want to print thousand and hundered number then what i to do 
# for that we use range function .

for n in range(6):
   print(n) 



# Another example 
names=['adeel','naveed','dilwar','husnain']
for name in names:
    print(f"Hello {name}")



#another example comes here 
name='adeel'
for character in name:
    print(character.capitalize())





# Nested for Loop

for i in range(3): #matlab k 0,1,2
    for j in range(2):
        print(f"i={i}, j={j}")


# jab i ki value 0 ho gi to wo under vale loop pr jaye ga waha pr ak or loop hai jo nijy print me wo i ki place par "0" put kary ga and j ki jaga "0" , pr abi under vala loop khatam nahi hoa osy ki value 2 (0,1) complete nahi ho jy gi os time tak under vala loop chalta rehy ga . ab doubara under vala loop call ho ga or doubara i =0 and j=1 print ho ga . Ab under vala loop complete hoa ab ewo doubara uper vale loop par jy ga doubra loop start ho jy ga .
#i=0, j=0
#i=0, j=1
#i=1, j=0
#i=1, j=1
#i=2, j=0
#i=2, j=1




# Another example created square root of a list of number 


square_number={f"square root of {x}":x**2  for x in range(10)}
print(square_number)








#===================> While loop <=========================
print("While Loop starting Here !")
count=0
while count < 5:
    print(count)
    count +=1


# it's print from 0 to 4 number first line initialize the variable by zero , 
# And 2nd line has a while loop where we provide a condition when ever it's true the loop keep starting and when it's while loop is false it's stops 
# 3rd line show print it's print 0 at first time and then move to next line 
# 4 line add +1 in count now the count value is 1 not the zaro . 



