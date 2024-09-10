# Program to check the file size

import os

# Input the file path
file_path = input("Enter the file path: ")

# Get the file size in bytes
file_size = os.path.getsize(file_path)

# Display the file size
print(f"The size of the file is: {file_size} bytes")
