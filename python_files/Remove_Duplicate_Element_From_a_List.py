# Program to remove duplicate elements from a list

# Define a list with duplicate elements
my_list = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates by converting the list to a set and back to a list
unique_list = list(set(my_list))

# Display the list without duplicates
print("List after removing duplicates:", unique_list)
