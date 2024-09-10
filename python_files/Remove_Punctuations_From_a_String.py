# Program to remove punctuations from a string

# Define punctuations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Input a string
string = input("Enter a string: ")

# Remove punctuations
no_punct = ""
for char in string:
    if char not in punctuations:
        no_punct += char

# Display the string without punctuations
print(f"String without punctuations: {no_punct}")
