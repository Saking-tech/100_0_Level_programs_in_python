# Program to convert decimal to binary using recursion

def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end='')

# Input a decimal number
num = int(input("Enter a decimal number: "))

# Display the binary representation
print(f"The binary representation of {num} is: ", end='')
decimal_to_binary(num)
print()  # for newline
