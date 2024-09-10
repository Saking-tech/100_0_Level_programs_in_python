# Program to transpose a matrix

# Define a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Initialize the transpose matrix
transpose = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Transpose the matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

# Display the transposed matrix
print("Transposed Matrix:")
for r in transpose:
    print(r)
