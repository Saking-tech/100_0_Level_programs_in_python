# Program to append to a file

# Input file path
file_path = input("Enter the file path: ")

# Input the text to append
text = input("Enter the text to append: ")

# Append the text to the file
with open(file_path, 'a') as file:
    file.write(text + '\n')

# Confirm the text was appended
print(f"Text appended to {file_path}")
