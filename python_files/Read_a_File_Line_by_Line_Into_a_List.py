# Program to read a file line by line into a list

# Input file path
file_path = input("Enter the file path: ")

# Read the file line by line into a list
with open(file_path, 'r') as file:
    lines = file.readlines()

# Display the list of lines
print("Lines from the file:")
for line in lines:
    print(line.strip())
