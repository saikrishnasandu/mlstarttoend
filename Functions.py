#A function helps avoiding code repetition.
#  A function is a block of code which only runs when it is called.
#Creating a function is defined using the def keyword followed by function name and paranthesis:

def myfunc():
    print("Hello from a function")
myfunc()


#why use Functions

temp1=77
celsius = (temp1-32) * 5/9
print(celsius)

temp2=95
celsius2=(temp2-32) *5/9
print(celsius2)


# with functions

def F_to_C(fahrenheit):
    return(fahrenheit-32) * 5/9
print(F_to_C(98))
print(F_to_C(100))
print(F_to_C(89))

# Return Values

#Functions can send data back to the code that called them using the return statement.

def greeting():
    return "Hello from a function"
print(greeting())


def my_func2():
    pass


# Arguments

#Information can be passed into functions as arguments

def my_function(fname):
    print(fname + " Refsnes")
my_function("Email")
my_function("Tobis")
my_function("Linus")


#Parameter vs Argument


# A parameter is the variable listed inside parentheses in the function definition

# An argument is the actual value that is sent to the function when it is called.


def my_function(name):
    print("Hello ", name)

my_function("Emil")


#Number of arguments

#If your function expects 2 arguments,you must call it with exactly 2 argumnets
def my_function(fname , lname):
      print(fname + " " + lname)
my_function("Emil", "Refsnes")



## Default Parameter values

def my_function(name = "friend"):
    print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function()
my_function("linus")


def my_function(country = "Brazil"):
    print("I am from ", country)

my_function("Sweden")
my_function("Norway")
my_function()
my_function("India")
