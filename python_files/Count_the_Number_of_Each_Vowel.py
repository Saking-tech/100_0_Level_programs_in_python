# Program to count the number of each vowel

# Input a string
string = input("Enter a string: ").lower()

# Define vowels
vowels = 'aeiou'

# Count vowels
vowel_count = {v: string.count(v) for v in vowels}

# Display the count of each vowel
print("Vowel counts:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
