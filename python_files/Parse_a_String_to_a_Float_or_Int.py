# Program to parse a string to a float or int

# Input a string
string = input("Enter a string to parse: ")

# Try parsing the string to a float and int
try:
    float_value = float(string)
    int_value = int(float_value)
    print(f"String parsed as float: {float_value}")
    print(f"String parsed as int: {int_value}")
except ValueError:
    print("Invalid input for parsing")
