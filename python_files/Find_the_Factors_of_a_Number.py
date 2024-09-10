# Program to find the factors of a number

# Input a number
num = int(input("Enter a number: "))

# Find and display the factors
print(f"Factors of {num} are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
