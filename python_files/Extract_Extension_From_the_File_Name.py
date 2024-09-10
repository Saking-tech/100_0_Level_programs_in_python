# Program to extract extension from the file name

# Input the file name
file_name = input("Enter the file name with extension: ")

# Extract the file extension
file_extension = file_name.split('.')[-1]

# Display the file extension
print(f"The extension of the file is: {file_extension}")
