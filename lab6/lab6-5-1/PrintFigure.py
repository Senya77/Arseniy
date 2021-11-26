def PrintRectangle(a, b, file):
    new_file = open(file, 'w')
    new_file.write('Содержимое файла ' + file + '\n')
    for j in range(b):
        if j == 0 or j == (b - 1):
            new_file.write('* ' * a + '\n')
        else:
            new_file.write('* ' + '  ' * (a - 2) + '* ' + '\n')
    new_file.close()


def PrintSquare(a, file):
    new_file = open(file, 'w')
    new_file.write('Содержимое файла ' + file + '\n')
    for j in range(a):
        if j == 0 or j == (a - 1):
            new_file.write('* ' * a + '\n')
        else:
            new_file.write('* ' + '  ' * (a - 2) + '* ' + '\n')
    new_file.close()
