from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Фамилия призывника", "Иня призывника", "Отчество призывника", "Год рождения призывника",
                     "Заболевание призывника"]
number = int(input("Введите количество призывников "))
soldier = {}
for number in range(number):
    number += 1
    data = (input('Введите Фамилию Имя Отчество призывника №%d, год его рождения и заболевание ' % number).split())
    soldier["Фамилия"] = data[0]
    soldier["Имя"] = data[1]
    soldier["Отчество"] = data[2]
    soldier["год рождения"] = data[3]
    soldier["заболевание"] = data[4] + ' ' + data[5] + ' ' + data[6] + ' ' + data[7]
    table.add_row([soldier["Фамилия"], soldier["Имя"], soldier["Отчество"], soldier["год рождения"], soldier["заболевание"]])
print(table)
