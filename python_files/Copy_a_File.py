# Program to copy a file

import shutil

# Input source and destination file paths
source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")

# Copy the file
try:
    shutil.copy(source, destination)
    print(f"File copied from {source} to {destination}")
except Exception as e:
    print(f"Error: {e}")
