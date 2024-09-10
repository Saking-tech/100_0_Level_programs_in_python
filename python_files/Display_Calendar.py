# Program to display the calendar of a month and year

import calendar

# Input year and month
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Display the calendar
print(calendar.month(year, month))
