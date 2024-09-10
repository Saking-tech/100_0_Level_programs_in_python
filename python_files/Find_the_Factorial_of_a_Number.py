# Program to find the factorial of a number

# Input a number
num = int(input("Enter a number: "))

# Factorial of a number is not defined for negative numbers
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
