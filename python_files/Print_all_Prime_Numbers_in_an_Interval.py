# Program to print all prime numbers in an interval

# Input the start and end of the interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Iterate through the range
for num in range(start, end + 1):
    # Prime numbers are greater than 1
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
