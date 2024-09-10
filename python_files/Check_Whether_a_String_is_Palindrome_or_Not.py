# Program to check if a string is palindrome

# Input a string
string = input("Enter a string: ")

# Check if the string is the same forwards and backwards
if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
