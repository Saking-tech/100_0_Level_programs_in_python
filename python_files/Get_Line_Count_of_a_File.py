# Program to get the line count of a file

# Input the file path
file_path = input("Enter the file path: ")

# Count the number of lines
with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)

# Display the line count
print(f"The file has {line_count} lines")
