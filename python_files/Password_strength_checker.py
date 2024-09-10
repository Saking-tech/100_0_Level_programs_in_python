# Program to check password strength

import re

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password too short"
    if not re.search("[a-z]", password):
        return "Weak: No lowercase letters"
    if not re.search("[A-Z]", password):
        return "Weak: No uppercase letters"
    if not re.search("[0-9]", password):
        return "Weak: No digits"
    if not re.search("[@#$%^&*!]", password):
        return "Weak: No special characters"
    return "Strong password"

# Input password
password = input("Enter your password: ")

# Check and display password strength
print(check_password_strength(password))
