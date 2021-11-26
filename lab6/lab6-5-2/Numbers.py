def profnum(values):  # property of numbers(свойства чисел)
    if len(values) != 0:
        value = values[0]
        multi = 1
        summ = 0
        for i in value:
            summ += int(i)
            multi *= int(i)
        numbers = len(value)
        return "Число: {}\nКоличество цифр: {}\nСумма цифр: {}\nПроизведение цифр: {}".format(value, numbers, summ, multi)
    else:
        return 'Файл с входными данными нe обнаружен'
