a = float(input('Введите длину первой стороны '))
b = float(input('Введите длину второй стороны '))
c = float(input('Введите длину третьей стороны '))


def existence():
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


# existence проверяет возмоность существование треугольника

def type():
    if a == b == c:
        return 1
    elif (a == b) or (a == c) or (b == c):
        return 2
    else:
        return 3


# kind проверяет вид треугольника

if existence():
    if type() == 1:
        print("Треугольник равносторонний")
    elif type() == 2:
        print("Треугольник равнобедренный")
    elif type() == 3:
        print("Треугольник общего вида")
else:
    print("Треугольник не существует")
