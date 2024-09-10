# Program to sort a dictionary by value

# Define a dictionary
student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# Sort dictionary by value
sorted_scores = dict(sorted(student_scores.items(), key=lambda item: item[1]))

# Display the sorted dictionary
print("Dictionary sorted by value:", sorted_scores)
