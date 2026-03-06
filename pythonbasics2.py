# for loop

# Iterate over sequence of numbers

for i in range(5):
    print(i)



for i in range(1,10,2):
    print("number:",i)



for i in range(10,1,-1):
    print(i)



str = "Raghavayya"
for i in str:
    print("thatha:",i)



# While loop
    
# The while loop continues to eecute as long as the co9ndition is True.


count = 0

while count<5:
    print("while:",count)
    count+=1



# Loop control statements
    

# Break
    
 # The break statement exits the loop prematurely
    
#break statement
    

for i in  range(10):
    if i ==6:
      break
    print(i)



# continue
    
   #The continue statement skip the current iteration and continues with the next.
for i in range(10):
        if i%2==0:
         continue
        print(i)

# Pass 
        
        # Pass statement is a null operation: it does nothing

        for i in range(5):
            if i == 3:
                pass
            print(i)



# Nested loops
            # A loop inside a loop


for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")



# Examples  Calculate the sum of first N natural numbers using a while and for loop
        

        # While loop
n=10
sum = 0
count=1
while count<=n:
    sum = sum + count
    count = count + 1
print("sum of first 10 natural numbers: ", sum)




sum=0
for i in range(11):
    sum = sum+i
print(sum)

# Example Prime numbers between 1 and 100

for num in range(1,100):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
