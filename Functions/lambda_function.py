#Lambda function : lambda function is those function which don't need any specific function name , it's a short function 

#Syntax
#lambda arguments: expression like lambda x,y: x-y

add= lambda x,y : x-y
print(add(5,6))
#Argument meant by parameter and expression meant by what we do in out function ,

#Pactical example
# how to square of a list by using lambda function and map methode 
numbers1=[1,2,3,4,5,6,7]
squared=list(map(lambda x:x**2 , numbers1))
print(squared)


# we also used lambda function for filter the even or odd number 
filterevennumber=list(filter(lambda x:x%2 ==0 ,numbers1))
print(filterevennumber)
# here expolre how our function works , 
#filterevennumber=list(filter(lambda x:x%2 ==0 ,numbers1)) , first question raised here why we enter list in start of all the that because we already provide list above numbers1=[1,2,.....]
#Answer is that map funtion always return a object , to convert object into list we use list() in the start .
#and at the last ,numbers1 shows our lambda function assign on all element of this function .





#sorted function : it's set our function in different formate like in asending order or in desending order me by default it's on asending order .


#convert list in descending order and reverse it's by using reverse=true
sortingfuntion=list(sorted(numbers1,reverse=True))
print(sortingfuntion)

#we also shorting a list of string by albhabtecally 
abc=["adeel","naveed","adnan"]
print(sorted(abc))

#shorted by len
print(sorted(abc , key=len))

