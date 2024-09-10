# Program to check if a string is a number (float)

# Input a string
string = input("Enter a string: ")

# Check if string is a float
try:
    float_value = float(string)
    print(f"'{string}' is a number")
except ValueError:
    print(f"'{string}' is not a number")
