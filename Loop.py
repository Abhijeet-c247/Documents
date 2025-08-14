# For loop 

for i in range(5):
    print(i)
    
    
#---------------------------------------------------------------------------------------

# For loop with condition

for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
        
#---------------------------------------------------------------------------------------

# For loop with break

for i in range(10):
    if i == 5:
        print("Breaking the loop at 5")
        break
    print(i)
    
#---------------------------------------------------------------------------------------

# For loop with continue

for i in range(10):
    if i % 2 == 0:
        continue
    print(f"{i} is odd, skipping even numbers")
    
#---------------------------------------------------------------------------------------

# For loop with pass

for i in range(5):
   
        pass  # Placeholder for future code
    
#---------------------------------------------------------------------------------------

# While loop

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  
    
#---------------------------------------------------------------------------------------

# infinite loop with break

count = 0
while True:
    if count >= 5:
        print("Breaking the infinite loop")
        break
    print(f"Count is: {count}")
    count += 1
    
#---------------------------------------------------------------------------------------

# print table of any number with for loop

def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
        
num = int(input("Enter a number to print its table: "))
print_table(num)


#---------------------------------------------------------------------------------------