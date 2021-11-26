import os

from Eratosthenes import eratosthenes

if os.path.exists('/labs/lab6/lab6-5-3/input(6-5-3).txt'):

    input_file = open('input(6-5-3).txt', 'r')
    output_file = open('output(6-5-3).txt', 'w')

    n = int(input_file.readline())

    output_file.write(eratosthenes(n))
    input_file.close()
    output_file.close()

else:
    output_file = open('output(6-5-3).txt', 'w')
    output_file.write('Файл с входными данными нe обнаружен')
    output_file.close()
