# Program to check if a number is positive, negative, or zero

# Input a number
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is a positive number")
elif num == 0:
    print("The number is zero")
else:
    print(f"{num} is a negative number")
