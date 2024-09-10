# Program to iterate through two lists in parallel

# Define two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Iterate through both lists in parallel
for item1, item2 in zip(list1, list2):
    print(f"{item1} - {item2}")
