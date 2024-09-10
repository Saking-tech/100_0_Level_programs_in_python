# Program to find all files with .txt extension present inside a directory

import os

# Input the directory path
directory = input("Enter the directory path: ")

# List all .txt files in the directory
txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]

# Display the .txt files
print("Text files in the directory:")
for file in txt_files:
    print(file)
