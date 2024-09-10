# Program to safely create a nested directory

import os

# Input the directory path
dir_path = input("Enter the directory path: ")

# Safely create the directory
try:
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory {dir_path} created successfully")
except Exception as e:
    print(f"Error creating directory: {e}")
