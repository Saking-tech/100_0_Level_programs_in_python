# Program to find Armstrong numbers in an interval

# Input the start and end of the interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Iterate through the range
for num in range(start, end + 1):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    # Check if the number is an Armstrong number
    if num == sum:
        print(num)
