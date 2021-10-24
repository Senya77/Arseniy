Hopt = int(input('Введите часы отправления '))
Mopt = int(input('Введите минуты отправления '))
Hp = int(input('Сколько часов поезд будет в пути  '))
Mp = int(input('Сколько минут поезд будет в пути  '))


def time():
    days = Hp // 24
    MM = (Mopt + Mp) % 60
    if Mopt + Mp >= 60:
        HH = (Hopt + Hp + 1) % 24
    else:
        HH = (Hopt + Hp) % 24
    print('%d hours : %d minutes' % (HH, MM))
    print(days, 'days')


time()
