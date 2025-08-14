# Simple Function 

def Greeting():
    print("Hello, welcome to the function demonstration!")
    
Greeting()


#--------------------------------------------------------------------------------------

# Function with Parameters

def add_numbers(num1, num2):
    return num1 + num2 , num1 * num2 , num1 - num2

result = add_numbers(5, 3)
print(f"Sum: {result[0]}, Product: {result[1]}, Difference: {result[2]}")


# --------------------------------------------------------------------------------------

# Function with Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")
    
greet()  # Calls with default parameter
greet("Abhijeet")  # Calls with parameter

# --------------------------------------------------------------------------------------

# Function with Variable Number of Arguments
def display_info(*args):
    return sum(args)
        
result = display_info(1, 2, 3, 4, 5)
print(f"Sum of variable arguments: {result}")


# --------------------------------------------------------------------------------------
# Function with Keyword Arguments
def person_info(name, age, **kwargs):
    info = f"Name: {name}, Age: {age}"
    for key, value in kwargs.items():
        info += f", {key}: {value}"
    return info

result = person_info("Abhijeet", 25, city="Indore", occupation="Engineer")
print(result)

# --------------------------------------------------------------------------------------

# Function with Return Statement
def square(num):
    return num * num    

result = square(4)
print(f"Square of 4 is: {result}")

# --------------------------------------------------------------------------------------

# Function with Lambda Expression
square_lambda = lambda x: x * x
result = square_lambda(5)
print(f"Square of 5 using lambda: {result}")

# --------------------------------------------------------------------------------------

