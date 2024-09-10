# Program to convert string to datetime

from datetime import datetime

# Input a date string
date_string = input("Enter a date in the format YYYY-MM-DD: ")

# Convert the string to a datetime object
date_object = datetime.strptime(date_string, '%Y-%m-%d')

# Display the datetime object
print("Converted datetime object:", date_object)
