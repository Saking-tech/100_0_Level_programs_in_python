# Program to generate a random password

import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Input password length
length = int(input("Enter the length of the password: "))

# Generate and display the password
print(f"Generated password: {generate_password(length)}")
