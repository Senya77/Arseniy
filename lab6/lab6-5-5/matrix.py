
def matrix(N, M):
    import numpy as np
    import random
    K = random.randint(5, 15)
    matrix_A = np.random.randint(9, size=(N, M))
    matrix_B = np.random.randint(9, size=(M, K))
    return [matrix_A, matrix_B, matrix_A.dot(matrix_B)]


def matrix_division(N, M, mtrx, max_matrix):
    row = 0
    column = 0
    for i in range(N):
        for k in range(M):
            mtrx[row][column] = mtrx[row][column] // max_matrix[row]
            column += 1
        column = 0
        row += 1
    return mtrx
