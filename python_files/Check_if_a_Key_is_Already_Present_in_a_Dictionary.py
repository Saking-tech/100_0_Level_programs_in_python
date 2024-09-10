# Program to check if a key is already present in a dictionary

# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Input a key to check
key = input("Enter the key to check: ")

# Check if key is present
if key in my_dict:
    print(f"Key '{key}' is present in the dictionary")
else:
    print(f"Key '{key}' is not present in the dictionary")
