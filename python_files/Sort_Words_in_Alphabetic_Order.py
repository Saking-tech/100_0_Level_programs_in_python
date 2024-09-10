# Program to sort words in alphabetic order

# Input a string of words
string = input("Enter a string: ")

# Split the string into words and sort them
words = string.split()
words.sort()

# Display the sorted words
print("Words in alphabetical order:")
for word in words:
    print(word)
