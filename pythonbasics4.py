# Tuples

# Tuples are ordered collections of items that are immutable. They are similar to lists but their immutability makes them different

# create a tuple

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

lst=list()
print(type(lst))
tpl=tuple()
print(tpl)


numbers = tuple([1,2,3,4,5,6])
print(numbers)

mixed_tuple=(1,"Hello",3.14,True)
print(mixed_tuple)
print(type(mixed_tuple))


print(numbers[2])
print(numbers[-1])


print(numbers[0:5])

print(numbers[::-1])


concatenation_tuple= numbers + mixed_tuple
print(concatenation_tuple)


print(mixed_tuple*3)


print(numbers*4)


# Immutable Nature of Tuples

# Tuples are immutable means their elements cannot be changed once assigned

lst = [1,2,3,4,5]
print(lst)
lst[4]=6
print(lst)
#numbers[1]=4
print(numbers)

## Tuple Methods

print(numbers.count(1))
print(numbers.index(1))



# Packing and Unpacking tuple


packed_tuple = 1,"hello",3.14
print(packed_tuple)

# Unpacking a tuple

a,b,c = packed_tuple
print(a)
print(b)
print(c)


# Unpacking tuple with *
9
numbers=(1,2,3,4,5,6)
fruits,*middle,last=numbers
print(fruits)
print(middle)
print(last)



# Nested Tuple

lst=[[1,2,3,4],[6,7,8,9],[1,"hello",3.14,"m"] ] # Nested List
print(lst[0])

print(lst[0][0:3])
print(lst[2][0:3])


tpl=((1,2,3),("a","b","c"),(True,False))
print(tpl[0])
print(tpl[1][1:])

##  Iterating over nested tuple

for sub_tuple in tpl:
    for item in sub_tuple:
        print(item)



