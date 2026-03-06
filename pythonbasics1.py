no1= 29292
no2=9382
print(no1>=no2)


num1 = 3044
num2 = 3933
print(num1<+num2)


# Logical Operators

## And , Not, OR


# Both A and B are true  

X = True
Y = True

result = X and Y

print(result)


X = True
Y = False

result = X and Y
print(result)

# OR

# only false when both are false  else True


X = True
Y = False

result = X or Y
print(result)


# Not Operator

X = False
print(not X)




## if statement

#if statement eecutes when the condition becomes true

age = 20

if age>=18:
    print("You are eligible to vote")

print(age>18)


# else  
# else statement executes when the condition in the if statement is False

age = 16
if age>=18:
    print("you are eligible for voting")
else:
    print("you are minor")


# elif statement
    
    ## The elif statement allows you to check multiple conditions. It stands for  "else if"
age=int(input("enter the age: "))
if age<13:
        print("you are a child")
elif age<18 and age>13:
        print("you are a teenager")
else:
        print("you are an adult")



## Nested conditional statement
        
# you can place one or more if , elif, or else statements inside another if,elif or else statement to  create nested conditional statements.
        
        ## number even, odd and negative

num = int(input("Enter the number"))

if num>=0:
      print("The number is positive")
      if num%2==0:
            print("The number is even")
      else:
            print("The number is ODD")
else:
      print("number is zero or negative")

## Practiceal Examples
      
## Determineif a year is a leap year using nested condition statement
      
year = int(input("Enter the year:"))
if year%4==0:
        if year%100==0:
              if year%400==0:
                    print(year,"Is a leap year")
              else:
                    print(year,"Is not a leap year")
        else:
              print(year,"is a leap year")
else:
            print(year,"Is not a leap year")

