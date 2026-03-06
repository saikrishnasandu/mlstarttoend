# Lists

#Lists are ordered mutable collections of items.
# They can contain items of different data types.

lst = []
print(type(lst))


names=['shiva','krishna','sai',1,2,3]
print(names)


mixed_list=[1,"hello",3.14,True]
print(mixed_list)


# Accessing list Elements

fruits=["apple","Banana","cherry","kiwi","promo"]
print(fruits[0])
print(fruits[3])
print(fruits[-1])


print(fruits[1:])

print(fruits[1:3])

print(fruits[-1:-4:-1])

fruits[1]="Watermelon"
print(fruits)

fruits=["apple","Banana","cherry","kiwi","promo"]
## List Methods

fruits.append("orange")
print(fruits)


fruits.insert(1,"watermelon")

print(fruits)

fruits.remove("Banana")
print(fruits)

## Remove and return thr last element
popped_fruits=fruits.pop()
print(fruits)


ind=fruits.index("kiwi")
print(ind)

fruits.insert(2,"Banana")
fruits.insert(2,"Banana")
print(fruits.count("Banana"))
print(ind)
print(fruits)
print(ind)
xhs=fruits.index("kiwi")
print(xhs)

fruits.sort()  # Sort list i ascending order

print(fruits)


fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)


fruits=["apple","Banana","cherry","kiwi","promo"]
print(fruits)

# Slicing List

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])



num=numbers[::-2]
print(num)



for number in numbers:
    print(number)


# Iterating with index
    
    for index,number in enumerate(numbers):
        print(index,number)



# List comprehension
lst=[]
for x in range(5):
            lst.append(x**2)
print(lst)



print([x**2 for x in range(10)])


### List comprehension

#Basic Syntax  [expression for item in iterable]

# with conditional logic   [expression for item i iterable if condition]


## Basic List comprehension


square = [num**2 for num in range(6)]
print(square)



## List comprehension with condition
lst1=[]
for i in range(9):
       if i%2==0:
        lst1.append(i**2)
print(lst1)



even_numbers=[num for num in range(7) if num%2==0 ]
print(even_numbers)

for j in range(ord('a'),ord('z')+1):
      
      print(chr(j),end=" ")
     
lst2=[1,2,3,4]
lst3=['a','c','d','e']
pair=[[i,j] for i in lst2 for j in lst3]
print(pair)



## List comprehension with function calls


words = ["hello","world","python","List","comprehension"]
lengths=[len(word) for word in words]
print(lengths)
