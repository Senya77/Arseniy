import numpy as np

from matrix import matrix, matrix_division

input_file = open('input(6-5-5).txt', 'r')
N = int(input_file.read(1))
M = int(input_file.read(2))
input_file.close()

result = matrix(N, M)
max_matrix_A = np.max(result[0], axis=1)

output_file = open('output(6-5-5).txt', 'w')

output_file.write("Матрица A: " + "\n")
for i in result[0]:
    output_file.write(" ".join(map(str, i)) + "\n")

output_file.write("Матрица A, деленная на максимальное число в каждой строке: " + "\n")
for i in matrix_division(N, M, result[0], max_matrix_A):
    output_file.write(" ".join(map(str, i)) + "\n")

output_file.write("Матрица B: " + "\n")
for i in result[1]:
    output_file.write(" ".join(map(str, i)) + "\n")

output_file.write("Матрица A*B: " + "\n")
for i in result[2]:
    output_file.write(" ".join(map(str, i)) + "\n")

output_file.close()
