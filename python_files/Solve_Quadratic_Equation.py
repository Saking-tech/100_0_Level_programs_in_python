# Program to solve a quadratic equation

# Import the math module for square root function
import math

# Input coefficients of the quadratic equation ax^2 + bx + c = 0
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Find two solutions
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"The solutions are {root1} and {root2}")
elif d == 0:
    root = -b / (2 * a)
    print(f"The solution is {root}")
else:
    realPart = -b / (2 * a)
    imagPart = math.sqrt(-d) / (2 * a)
    print(f"The solutions are {realPart}+{imagPart}i and {realPart}-{imagPart}i")
