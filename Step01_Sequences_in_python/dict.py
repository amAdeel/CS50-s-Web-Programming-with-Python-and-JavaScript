#==========================> What is dict in pythone <================================
### DICT stand for dictionary , and it's collecct for key value pair , each key is unique and have a specific value .
#it's like a object in in typescript 


my_information={'name':'Adeel' , 'father name':'Muhammad Ashraf' , 'class' : 'Bs 4 semester' , 'address' : ' Kuolsar colony adda gamber okara cantt', 'age': 25 , 'mobile': +923227711450}
print(my_information)


print(my_information["name"])# here we say go to name section and collect name value the [] bracket work like a jase hum index number dety ty and value print karty ty , same here hum yaha key provide kary gy and value print karvay gy 



print(my_information["class"])


# it's work on a unique element when i try to used two same key at same point then it's select 2nd value .




# Mutable: mean we can change value init .

my_information["age"]=35
print(my_information)



# NOW discuss methode that used in dict 
# get(key)
# key()
# value()
# item()
# update()
# pop(key)
# clear() 



# get(key) it's return the value of the key 
print(my_information.get('father name')) #trough key 
print(my_information["father name"]) #through []


# key() it's also a build in function that return all the key present in our dict
print(my_information.keys())



#values() it's retuen all the values of the key's 
#items() it's return all key's and value 
print(my_information.items())



#update() here we update multiply key and it's value 


# pop(key)
copy_my_information=my_information.copy()
print(copy_my_information.pop("name"))
print(copy_my_information)
# Here we first copy the dict and form a new  dict and then remove a name from my dict set by pop(key methods)