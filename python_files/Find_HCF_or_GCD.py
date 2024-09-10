# Program to find HCF or GCD of two numbers

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Function to compute HCF or GCD
def compute_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

# Display the HCF or GCD
hcf = compute_hcf(num1, num2)
print(f"The HCF or GCD of {num1} and {num2} is {hcf}")
