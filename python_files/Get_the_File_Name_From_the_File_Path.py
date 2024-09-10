# Program to get the file name from the file path

import os

# Input the file path
file_path = input("Enter the file path: ")

# Get the file name from the path
file_name = os.path.basename(file_path)

# Display the file name
print(f"The file name is: {file_name}")
