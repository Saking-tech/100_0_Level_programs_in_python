import os

# Path to the file containing the titles
title_file_path = 'python_files\\title.txt'

# Directory to save the Python files
output_directory = 'python_files'
os.makedirs(output_directory, exist_ok=True)

# Read the titles from the file
with open(title_file_path, 'r') as file:
    titles = file.readlines()

# Create an empty .py file for each title
titles = titles[88:101]
for title in titles:
    # Strip any leading/trailing whitespace and replace spaces with underscores
    sanitized_title = title.strip().replace("\n", " ")

    # Remove any characters that are not alphanumeric or underscores for filename safety
    sanitized_title = "".join(char for char in sanitized_title if char.isalnum() or char == '_')

    # Append the .py extension to create the filename
    file_name = sanitized_title + ".py"
    file_path = os.path.join(output_directory, file_name)
    
    # Create the file
    with open(file_path, 'w') as py_file:
        pass  # Just create an empty file

print("Python files have been created successfully.")