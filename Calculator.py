First_Number = float(input("Enter the first number: "))

operator = input("Enter an operator (+, -, *, /): ")

Second_Number = float(input("Enter the second number: "))

if operator == '+':
    result = First_Number + Second_Number
elif operator == '-':
    result = First_Number - Second_Number
elif operator == '*':
    result = First_Number * Second_Number
elif operator == '/':
    if Second_Number != 0:
        result = First_Number / Second_Number
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."
    
print(f"The result of {First_Number} {operator} {Second_Number} is {result}")
