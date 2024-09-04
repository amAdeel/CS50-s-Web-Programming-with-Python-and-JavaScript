#=========================================> What is tuples <=====================================
### tuple is similar to list but it's can't be change able . it's also used for grouping of different value and assign to a sign unit lime that (40.7128, -74.0060): "New York",

#syntax
fruits=("apple","mango","banana","Pineapple","cherry","graps")
print(fruits[3])

# now chack it's mutable or not it's cant allow us to make change init.
# fruits[3]="doubleApllle"
# print(fruits) it's shows error because in tuple we can't change the value ones it's define .

## in tuple we also used other methode also of all the list like that how slice ,

(first,second,third,four,five, six)=fruits
print(first)


#practical example
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (51.5074, -0.1278): "London",
    
}
print(locations[(40.7128, -74.0060)])

