try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))    # Input numbers from user
    result = num1 / num2                             # Perform division operation 
except ValueError:
    print("Error: Please enter only numbers!")      # If input is not a number
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")        # If division by zero occurs

else:
    print(f"Result = {result}")                 # If no exceptions, this will execute
finally:
    print("Thank you for using the calculator.")   # This line will always execute