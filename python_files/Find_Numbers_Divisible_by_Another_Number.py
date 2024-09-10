# Program to find numbers divisible by another number in a range

# Input the range and the divisor
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
divisor = int(input("Enter the divisor: "))

# Find and display divisible numbers
for num in range(start, end + 1):
    if num % divisor == 0:
        print(num)
