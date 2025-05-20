def matrMult(A, B): # Takes in 2 matrices as nested lists, returns the matrix multiplication of the given matrices, if possible.
    # Get the dimensions of the matrices.
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if multiplication is possible.
    if cols_A != rows_B:
        return []

    # Initialize a zero matrix with given dimensions.
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform the matrix multiplication.
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

"""
# Example usage:
A = [[1, 2, 3, 4], 
     [5, 6, 7, 8]]

B = [[5,  6,   7], 
     [8,  9,  10], 
     [11, 12, 13], 
     [14, 15, 16]]

print(matrMult(A, B))

C = [[110, 120, 130],
     [262, 288, 314]]
"""