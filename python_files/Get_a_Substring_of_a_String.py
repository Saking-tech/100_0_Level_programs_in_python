# Program to get a substring of a string

# Input a string
string = input("Enter a string: ")

# Input the start and end indices
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

# Get the substring
substring = string[start:end]

# Display the substring
print("Substring:", substring)
