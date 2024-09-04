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
print(my_Ip_address)




# USECASE 
#it's use for quickly remove a duplicate from a list and tuples 
set3 = [ 1,1,1,1,2,2,2,2,4,4,5,5,5,5,6,7,7]
usecase=list(set(set3))
print(usecase)

#Memebership present or not
print(5 in set3)
