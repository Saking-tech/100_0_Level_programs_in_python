# Program to check if two strings are anagram

# Input two strings
str1 = input("Enter the first string: ").lower()
str2 = input("Enter the second string: ").lower()

# Check if the two strings are anagrams
if sorted(str1) == sorted(str2):
    print(f"'{str1}' and '{str2}' are anagrams")
else:
    print(f"'{str1}' and '{str2}' are not anagrams")
