Name = "Abhijeet"  # string variable
Age = 25           # integer variable
CGPA = 8.1         # float variable

print("Name:", Name)  # printing the string variable
print("Age:", Age)    # printing the integer variable
print("CGPA:", CGPA)  # printing the float variable

print(type(Name))  # printing the type of the string variable
print(type(Age))   # printing the type of the integer variable
print(type(CGPA))  # printing the type of the float variable

age = input("Enter your age : ")  # input function

int(age) # converting the string to an integer

age = int(input("Enter your age : "))  # input function with conversion

if age >= 18:  # if statement
    print("You are an adult. you can vote.")
else:  # else statement
    print("You are not an adult. you cannot vote.")
    
list = [1, 2, 3, 4, 5]       # list variable
for i in list:               # for loop
    if i == 3:               # if statement inside for loop
        continue             # continue statement
    elif i == 4:             # elif statement inside for loop
        break                # break statement
    else:                    # else statement inside for loop
        print(i)             # printing the value of i
        
