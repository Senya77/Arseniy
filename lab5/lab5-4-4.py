money = int(input('Введите сумму покупок '))


def rubles():
    cop = money % 100
    rub = money // 100
    if rub > 0:
        if rub % 10 == 1:
            print('%d' % rub, 'РУБЛЬ')
        elif (rub % 10 == '0', '5', '6', '7', '8', '9') or (10 <= rub <= 20):
            print('%d' % rub, 'РУБЛЕЙ')
        else:
            print('%d' % rub, 'РУБЛЯ')
    if cop > 0:
        if cop % 10 == 1:
            print('%d' % cop, 'КОПЕЙКА')
        elif (cop % 10 == '0', '5', '6', '7', '8', '9') or (10 <= cop <= 20):
            print('%d' % cop, 'КОПЕЕК')
        else:
            print('%d' % cop, 'КОПЕЙКИ')


rubles()
