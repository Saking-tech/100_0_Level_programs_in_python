# Program to display Fibonacci sequence using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input number of terms
n_terms = int(input("Enter the number of terms: "))

# Display the sequence
if n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n_terms):
        print(fibonacci(i), end=' ')
