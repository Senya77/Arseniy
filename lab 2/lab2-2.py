# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))   # Вывод типа переменной number
print()

float_number = 9.0
float_number = int(float_number)
print(float_number)

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов

first = 8
second = 5.5
third = '3'

print(type(first), type(second), type(third), sep='\n')

first = str(first)
second = int(second)
third = float(third)
print()

print(type(first), type(second), type(third), sep='\n')

# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.
