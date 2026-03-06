
# Dictionaries

'''Dictionaries are unordered collections of items.They store data in key_value pairs.keys must be unique and immutable
(eg.strings,numbers or tuples), while values can be of any type'''

#  Creating Dictionaries

empty_dict={}
print(type(empty_dict))

set1={}
print(type(set1))



# Key should be unique

student={"name":"krish","age":32,"grade":24}
print(student)
print(type(student))


# Error  --> Single key always used

#student={"name":"krish","age":32,"grade":24,"name":"sai"}
#print(student)

# Accessing dictionary elements

student={"name":"krish","age":32,"grade":24}

print(student['grade'])
print(student['name'])


# Accessing using get() method

print(student.get('grade'))

print(student.get('last_name'))
print(student.get('last_name','doesnt exist'))

# Modifying dictionary elements

# Dictionary are mutable , so ypou can add update or delete elements

print(student)


student["age"]=33  ## update value for a key
student['address']="India"    # added a new key and value


print(student)


del student['grade']  # delete key value pair
print(student)

## dictinory methods

keys=student.keys()  # get all the keys
print(keys)
values=student.values()  # get all the values
print(values)

items=student.items()  ## get all the key value pairs
print(items)



## shallow copy

student_copy=student # this is a wrong to copy a variable bcz if the changes are made in parent variable those willbe reflected in child variable
student['name']="sai"
print(student)
print(student_copy)



# so to avoid this 

student_copy1=student.copy()  # shallow copy syntax
print(student)
print(student_copy1)


student["name"]="krish3"

print(student)
print(student_copy)
print(student_copy1)



## Iterating over dictionaries
## you can use loops to iterate over dictionaries,keys,values or items



## Iterating over keys

for keys in student.keys():
    print(keys)


## Iterate over values
    
for value in  student.values():
        print(value)



## Iterate over key value pairs
        
for key,value in student.items():
      print(f"{key}:{value}")



##  Nested Dictionaries
      
students5={
      "students1":{"name":"krish","age":32},
      "students2":{"name":"peter","age":44}

}

print(students5)


## Access nested dictionaries elements
print(students5["students2"]["name"])
print(students5["students2"]["age"])




## Iterating over nested dictionaries

for student_id,student_info in students5.items():
      print(f"{student_id}:{student_info}")
      for key,value in student_info.items():
            print(f"{key}:{value}")



## Dictionary comphrehension
            

square={x:x**2 for x in range(5)}
print(square)



# conditional dictionary comphrehension

even={x:x**2 for x in range(10) if x%2==0}

print(even)

## Practical Examples

# use a dictionary to count the frequency of elements i list
numbers=[1,2,3,3,3,3,4,4,4,5,5,5,5,1]
frequency={}
for n in  numbers:
      if n in frequency:
            frequency[n]+=1
      else:
            frequency[n]=1
print(frequency)


dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merge_dict={**dict1,**dict2}
print(merge_dict)