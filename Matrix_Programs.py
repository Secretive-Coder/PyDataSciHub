#--Matrix Programs--
#Program 1
def add_matrices(mat1, mat2):
    result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = add_matrices(matrix1, matrix2)
print("Result after adding two matrices:")
for row in result:
    print(row)



#Program 2
    # Function to multiply two matrices
def multiply_matrices(mat1, mat2):
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = multiply_matrices(matrix1, matrix2)
print("Result after multiplying two matrices:")
for row in result:
    print(row)



#Program 3
    # Function to find the product of two matrices
def matrix_product(mat1, mat2):
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_product(matrix1, matrix2)
print("Result of the matrix product:")
for row in result:
    print(row)



#Program 4
    # Function to subtract two matrices
def subtract_matrices(mat1, mat2):
    result = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
subtraction_result = subtract_matrices(matrix1, matrix2)
print("Result after subtracting two matrices:")
for row in subtraction_result:
    print(row)



#Program 5
    # Function to transpose a matrix in a single line
def transpose_matrix(mat):
    result = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return result

original_matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(original_matrix)
print("Original Matrix:")
for row in original_matrix:
    print(row)
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)



#Program 6
    # Function to create an n*n matrix
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    return matrix

size = 3
result_matrix = create_matrix(size)
print(f"{size}x{size} Matrix created:")
for row in result_matrix:
    print(row)



#Program 7
    # Function to get the Kth column of a matrix
def get_kth_column(mat, k):
    result_column = [row[k] for row in mat]
    return result_column

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k_value = 1
result_column = get_kth_column(matrix, k_value)
print(f"{k_value}th column of the matrix:")
print(result_column)



#Program 8
    # Function to vertically concatenate two matrices
def vertical_concatenation(mat1, mat2):
    result = mat1 + mat2
    return result

# Example usage:
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
concatenated_matrix = vertical_concatenation(matrix1, matrix2)
print("Result after vertically concatenating two matrices:")
for row in concatenated_matrix:
    print(row)
