#=========================> What is List ? <============================================
## list is collection of data that are order and change and modify after creation 
#synax 
numbers=[1,2,3,4,5,6,7,8,9,10]

## key concept 

#get a number from the list by the help of index number it's start from 0 ...
print(numbers[3])

###Mutable
#It's changeable code 
temp_numbers=numbers[:]#make a copy a list , other way n1=n.copy() , n1=list(n)
print(temp_numbers)
temp_numbers[1:3]=25,26,27# it's target and make slice of starting:1 and ending:2 and then replace this number
print(temp_numbers)

## slicing

# hows slicing works in a list methode list[start:end:step] what its mean now we move further when start showing where the start a slice , 2nd end where the end the slice and 3rd slicise how many element skip after each element 

#list [start] what will me printed 
print(f"List start[2:] : {numbers[2:]}")
#it's shows list start after the index number 2 

#list[end]
print(f"List-end[:2] : {numbers[:2]}")


#list[start:end:step] all together now check what happend now 
print(f"List[3:11:1] : {numbers[3:11:2]}")
#another thing when we put 1 in step , it's cant be working because 1 is defualt selected in 



### one most important concept how to reverse a list ?
## for that purpose we also use slice methode 

print(f"reverse a list : {numbers[::-1]}")

#now expolre how's it's work here we ::-1 it's mean i don't care what comes in starting point you start where you want and 2nd : show i don't care where you end you can end anywhere , but at last we use -1 which show the reverse order for moving .



### one more thing in it if i want to copy my original list and change in my temperary list ?
## for that purpose we use three methode like 
#1st temp_numbers=number[:]
#2nd temp_numbers=numbers.copy()
#temp_numbers=list(numbers)



### Finding length of the list
print(f"legnth of the list : {len(numbers)}")



### if we want to adding or remove something in our a list 
#append() function for adding something 
#remove() funtion is used for removing a element
numbers.append(11)
print(numbers)
numbers.remove(11)
print(numbers)