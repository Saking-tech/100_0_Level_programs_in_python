# Program to check if a number is an Armstrong number

# Input a number
num = int(input("Enter a number: "))

# Find the sum of the cubes of its digits
order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check if the number is an Armstrong number
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
