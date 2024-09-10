# Program to find sum of natural numbers using recursion

def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)

# Input a positive integer
n = int(input("Enter a positive integer: "))

# Display the sum
if n <= 0:
    print("Please enter a positive integer")
else:
    print(f"The sum of the first {n} natural numbers is {sum_of_natural_numbers(n)}")
