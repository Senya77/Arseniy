from PrintFigure import PrintSquare, PrintRectangle

f = open('input(6-5-1).txt', 'r')
values = f.readline().split()
file = f.readline()
f.close()

a = int(values[0])

if len(values) == 2:
    b = int(values[1])
else:
    b = 0
if b == 0:
    PrintSquare(a, file[1:len(file) - 1])
else:
    PrintRectangle(a, b, file[1:len(file) - 1])
