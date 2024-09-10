# Program to count the occurrence of an item in a list

# Define a list
my_list = [10, 20, 10, 30, 10, 40, 50]

# Input the item to count
item = int(input("Enter the item to count: "))

# Count the occurrences of the item
count = my_list.count(item)

# Display the count
print(f"The item {item} appears {count} times in the list")
