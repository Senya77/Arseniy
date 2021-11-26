import os

from Numbers import profnum

if os.path.exists('/labs/lab6/lab6-5-2/input(6-5-2).txt'):
    input_file = open('input(6-5-2).txt', 'r')
    output_file = open('output(6-5-2).txt', 'w')

    values = input_file.readline().split()

    output_file.write(profnum(values))
    input_file.close()
    output_file.close()
else:
    output_file = open('output(6-5-2).txt', 'w')
    output_file.write('Файл с входными данными нe обнаружен')
    output_file.close()
