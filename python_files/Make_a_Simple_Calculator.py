# Simple calculator program

# Define functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Select operation
print("Select operation: +, -, *, /")
operation = input("Enter operation: ")

# Perform the operation
if operation == '+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '-':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == '*':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operation")
