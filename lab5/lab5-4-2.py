from math import sqrt

a = float(input('Введите коэффицент а квадратного уравнения '))
if a == 0:
    print('a не должно ровняться 0')
    a = float(input('Введите коэффицент а квадратного уравнения '))
b = float(input('Введите коэффицент в квадратного уравнения '))
c = float(input('Введите коэффицент с квадратного уравнения '))


def discriminant():
    D = b*b - 4*a*c
    return D


def root_x1():
    x1 = (-b + sqrt(discriminant())) / (2 * a)
    return x1


def root_x2():
    x2 = (-b - sqrt(discriminant())) / (2 * a)
    return x2


print('Уравнение', '(%.5f)*x^2+(%.5f)*x+(%.5f)=0' % (a, b, c), sep='\n')
if discriminant() < 0:
    print('Количество корней: 0')
elif discriminant() == 0:
    print('Количество корней: 1', '%.5f' % root_x1(), '%.5f' % root_x2(), sep='\n')
elif discriminant() > 0:
    if root_x1() > root_x2():
        root_x1, root_x2 = root_x2, root_x1
    print('Количество корней: 2', '%.5f' % root_x1(), '%.5f' % root_x2(),  sep='\n')
