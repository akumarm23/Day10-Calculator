# Simple Calculator Version 0.1

# Importing the calculator logo and the sys module for system-related functionality
from logo import logo
import sys

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract two numbers
def subtract(n1, n2):
    return n1 - n2

# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2

# Function to divide two numbers
def divide(n1, n2):
    # Check for division by zero
    if n2 == 0:
        return "Cannot divide by zero."
    return n1 / n2

# Dictionary mapping operation symbols to their respective functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Function to perform calculator operations
def calculator():
    # Displaying the calculator logo
    print(logo)
    
    # Getting the first number from the user
    num1 = float(input("Enter the first number, n1 = "))
    
    # Displaying available operation symbols
    for symbol in operations:
        print(symbol)

    # Flag to control the calculator loop
    should_continue = True

    # Main calculator loop
    while should_continue:
        # Getting the desired operation from the user
        operation_symbol = input("Pick an operation from above: ")

        # Getting the second number from the user
        num2 = float(input("Enter the second number, n2 = "))

        # Checking if the operation symbol is valid
        if operation_symbol not in operations:
            print("Invalid operation symbol. Please choose from the available symbols.")
            continue

        # Performing the calculation using the selected operation
        calculate = operations[operation_symbol]
        answer = calculate(num1, num2)

        # Displaying the result of the calculation
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Asking the user if they want to continue with the result or exit
        new_number = input(f"Type 'y' to calculate with {answer}; else type 'n' to EXIT \n").lower()

        # Updating num1 for the next iteration or exiting the calculator
        if new_number == 'y':
            num1 = answer
        else: 
            should_continue = False
            print("Thank you for using My Calculator :)\n")
            sys.exit()

# Calling the calculator function to start the program
calculator()

# END OF CODE v0.1
