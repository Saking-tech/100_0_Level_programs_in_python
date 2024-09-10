# Program to display the multiplication table

# Input the number for which the table is to be displayed
num = int(input("Enter the number: "))

# Display the multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
