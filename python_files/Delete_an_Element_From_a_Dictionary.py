# Program to delete an element from a dictionary

# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Input the key to delete
key = input("Enter the key to delete: ")

# Delete the key if present
if key in my_dict:
    del my_dict[key]
    print(f"Key '{key}' deleted from the dictionary")
else:
    print(f"Key '{key}' not found in the dictionary")
