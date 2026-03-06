# sets 

""" Sets are a  built in data type used to store collections of unique items. 
They are unordered mean no specific order and dont allow duplicate"""


# create a set 

my_set = {1,2,3,4}
print(my_set)
print(type(my_set))

my_sset=set([1,2,3,4,4,5,6,6,7])
print(my_sset)




# Basic set operation

# add and remove elements


my_sset.add(8)
print(my_sset)


my_sset.remove(5)
print(my_sset)

#my_sset.remove(10)


my_sset.discard(11)
print(my_sset)


# pop method

removed_element = my_sset.pop()
print(removed_element)
print(my_sset)


## clear all elements

my_sset.clear()
print(my_sset)



# Set membership test

num = {1,2,3,4,5}
print(3 in num)
print(45 in num)

# Mathmetical operation

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}


##  Union

union_set=set1.union(set2)
print(union_set)



#  Intersection 

intersection_set =set1.intersection(set2)
print(intersection_set)


set1.intersection_update(set2)
print(set1)

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

print(set1.difference(set2))
print(set2.difference(set1))


## Symmetric difference 

print(set1.symmetric_difference(set2))


# set methods

set1 = {1,2,3,4,5}
set2={3,4,5}

## is subset

print(set1.issubset(set2))

# is superset

print(set1.issuperset(set2))


lst=[1,2,2,3,4,4,5]
p=set(lst)
print(p)



## count unique words in text

text="In this tutorial we are discussing about set"

words=text.split()
unique_words=set(words)
print(unique_words)
print(len(unique_words))