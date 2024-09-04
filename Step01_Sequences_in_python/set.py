#===================> what is set in python <================================
#SET is collection of unique valua , that mean that can't collect any duplicate element , if the find a duplicate element they automatically remove this element .
#SYNTAX
# we can create a empty set 
s=set()
s.add(1)
s.add(2)
s.add(3)
print(s)


my_set={1,2,3,4,4,5}
print(my_set)
#//{1,2,3,4,5} can't show 4 two time.



# Mutable mean i can change value after the creation .
my_set.add(6)
print(f"Add a number 6 : {my_set}")
my_set.remove(6)
print(f"remove a number 6 : {my_set}")



####set is non indexing
## set is non indexing like we can't exces each element sepreately .
#print(my_set[1])
#it's can't be work like that .



### PYTHON SET is like a mathmaticlly set value like we can add to set interect two set , differnce two set 
#union(): Returns a new set with all elements from both sets.
#intersection(): Returns a new set with only the elements that are in both sets.
#difference(): Returns a new set with elements in the first set but not in the second.
#symmetric_difference(): Returns a new set with elements in either set but not in both.

set1={1,2,3,4,5}
set2={4,5,6,7,8}
union_set=set1.union(set2)
print(union_set)
intersection_set=set1.intersection(set2)
print(intersection_set)
differnce_set=set1.difference(set2)
print(differnce_set)
symmetric_set=set1.symmetric_difference(set2)
print(symmetric_set)

#SET OPeration

print(set1 | set2)  # Union: {1, 2, 3, 4, 5,6 ,7,8}
print(set1 & set2)  # Intersection: {4,5}
print(set1 - set2)  # Difference: {1, 2,3}
print(set1 ^ set2)  # Symmetric Difference: {1, 2, 3, 6, 7, 8 }


# Frozen Set
#frozen set is immutable version of set one we made a set a frozelset then we cant add or remove anthing from set.
my_Ip_address=frozenset({1234567890,4567888})
print(f"my_Ip_address\n\n")


# we convert a list into set 
randomlist=[1,2,3,3,4,4,4,5,5,5,5,5,6,6,7,7,9,8,8,8,8,10]# create a random list 
print(f"list of dublicate Number: {randomlist}")
convert_list_into_set=set(randomlist)
print(f"convert_list_into_set : {convert_list_into_set}\n\n")





# USECASE 
#it's use for quickly remove a duplicate from a list and tuples 
set3 = [ 1,1,1,1,2,2,2,2,4,4,5,5,5,5,6,7,7]
usecase=list(set(set3))
print(usecase)

# Memebership present or not
# like have 1000 of student name i find my student date in list first convert in to set and then print date in set it's return ture of false statement .
print(5 in set3)




#===============> practical example to check student are in or not <===============================

student_names = [
    "Ayesha Khan",
    "Ali Ahmed",
    "Riya Sharma",
    "Arjun Singh",
    "Sara Malik",
    "Rahul Verma",
    "Zara Ali",
    "Hassan Raza",
    "Meena Patel",
    "Adil Sheikh",
    "Fatima Tariq",
    "Kabir Hussain",
    "Sana Mir",
    "Ishaan Kumar",
    "Zainab Iqbal",
    "Rohan Gupta",
    "Nida Anwar",
    "Aman Gill",
    "Mahnoor Zafar",
    "Imran Siddiqui",
    "Adeel Ashraf"
]
search_your_name=input("Find Your Name :")# input required from user
### here comes two possibility you see above our names in final list is first character capital alway but user dont konw that HOW to entar 
# user may enter name in small later or enter all words in capital latter
# then we build a logic that convert first latter of each words in capital latter and convert other in samll latter .

# the input we get is singal string value with some space comes ,// adeel ashraf
# first task is that convert the string into a list of two words , // ["adeel","ashraf"]
   #=> for that we use  { split_word=search_your_name.split() }   split is a  build-in functions that saprate a string and () empty shows saprate on behalf of space , where he found space function splite the word . splite function return a list of string // ["adeel","ashraf"].
# then we use a for loop in access each word sparately and 
   #=> then goes to first word and access first character and captilized this character . its return // A for first word
   # => then access remaining words and convert it in lower-case  {  second_charcter=i[1:].lower() }  1: show make a slice of a list that starting from 1 index. // deel
   #=> then we join both word into a singal variable and append it into a empty string  .
   #=> here the first loop ends then goes to 2nd word and reapeat all the process 
# at last we get a list of names // ["Adeel","Ashraf"] from ["adeel","ashraf"] now it's time to reconvert it into a singal staring based on space 
    #=>  { joined_string=" ".join(captilized_input) } here we create a another variable name join list into it the " ".join(list) mean join a list on the behalf of space 

 
### captalize first world comes that 
captilized_input =[]
split_word=search_your_name.split()
# print(split_word)
for i in split_word:
 first_character=i[0].capitalize()
 second_charcter=i[1:].lower()
 first_word= first_character + second_charcter
 captilized_input.append(first_word)
# print(captilized_input)
# now we want to rejoin list of name in to a singal string by using space 
joined_string=" ".join(captilized_input)
# print(joined_string)
if joined_string in student_names:
    print(f"Congraturation {joined_string} ! your are selected for Desire Post . Best of Luck")
else:
    print(f"Sorry {joined_string} ! Better luck for Next time .")



