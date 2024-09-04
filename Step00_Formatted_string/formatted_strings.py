# name=input("Name: ")
# print(name)
# #Another way how to use this name in combination 
# print("Hello, "+  name)

# #Another methode to concedinate a string we use f string which is also called f string stand for formated strings. formatted string is used ("a formatted string is a way to embed expression inside string literals, using palceholder {} like how embedded value are represented")


# ## Here is the few method how to use formatted string .

# #first method is to used .format()
# age=30
# formatted_string= "my Name is {} and my age is {}.".format(name, age)
# print(formatted_string)


#======================>  using F-string  <========================================================
# #2 method is f=string method f string mean formatted string litrals , we used f before the string started
# my_father_name="Ashraf"
# occupation="Govt officer"
# formatted_string_1=f"My father name is {my_father_name} and his occupation is {occupation}"
# print(formatted_string_1)

#==========================>  using % and how's it's work <======================================

# 3 Another method to using % sign ,%s show the expression comes here is a string . and %d show the expression comes here is the number or integer or a decimal number

# formatted_string_2="my father name is %s and his occupation is %s ." %(my_father_name,occupation)
# print("formatted_string_2 :"+ formatted_string_2)

# explore more what can we do by this 
#%d for integer 
age1=35
print_age_1=('you are %d year old .')%age1
print(print_age_1)
#%f for float value
balance=25.4567
print_balance=('your current balance is %f')%balance
print(print_balance)

#%x convert a number into hexadecimal number which base is 16 by this feature we can convert a RGB color into a specific formate of hexedecimal number.
number=255
print_number=('the current number is %d and its hexa-decimal number is %x')%(number,number)
print(print_number)

#%o convert into octet number 
number1=255
print_number1=('the current number is %d and its octect-decimal number is %o')%(number1,number1)
print(print_number1)

#%e convert large number into small number by using this %e which convert a number into scientifical number .
number3=10000000000
print_number3=("the orginal number is this %d and by using e sign this become is this %e")%(number3,number3)
print(print_number3)