# Program to catch multiple exceptions in one line

try:
    # Input a number
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")
