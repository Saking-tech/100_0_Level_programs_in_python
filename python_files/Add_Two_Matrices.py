# Program to add two matrices

# Define the matrices
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Initialize result matrix with zeros
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Add corresponding elements
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Display the result
print("Resultant Matrix after addition:")
for r in result:
    print(r)

