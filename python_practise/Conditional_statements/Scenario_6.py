# 6. Scenario:
# Develop a calculator that takes two numbers and an arithmetic operator from the user and returns the result. The program should handle invalid inputs gracefully.
# Task:
# Write a Python program that prompts the user for two numbers and an operator (e.g., +, -, *, /).
# Validates the user inputs to ensure the numbers are valid floats/integers and the operator is one of the allowed ones.
# Performs the calculation and displays the result.
# Handles division by zero and any other possible errors with appropriate messages.

def calculator():
    print("Welcome to the Simple Calculator!")

    # Get first number
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Get second number
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Get operator
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform calculation
    if operator == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operator == '/':
        try:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator! Please use one of +, -, *, /.")


# Run the calculator
calculator()
