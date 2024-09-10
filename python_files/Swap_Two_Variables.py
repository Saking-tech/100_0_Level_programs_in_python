# Program to swap two variables

# Input two variables
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))


# Swap the values
x = x + y
y = x-y
x = x-y

# Display the swapped values
print(f"After swapping, the value of x is {x} and the value of y is {y}")
