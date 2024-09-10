# Program to count the number of occurrence of a character in a string

# Input a string
string = input("Enter a string: ")

# Input the character to count
char = input("Enter the character to count: ")

# Count the occurrences of the character
count = string.count(char)

# Display the count
print(f"The character '{char}' appears {count} times in the string")
