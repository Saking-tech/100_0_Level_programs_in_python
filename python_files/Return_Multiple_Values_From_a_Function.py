# Program to return multiple values from a function

# Define a function that returns multiple values
def calculate(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    return sum, difference, product

# Call the function and unpack the returned values
sum_val, diff_val, prod_val = calculate(10, 5)

# Display the results
print(f"Sum: {sum_val}, Difference: {diff_val}, Product: {prod_val}")
