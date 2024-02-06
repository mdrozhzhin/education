# Задание 1 - Вариант 11
import math

a = math.cos(int(input('Введите значение a: ')))
b = math.cos(int(input('Введите значение b: ')))
c = math.cos(int(input('Введите значение c: ')))
d = math.cos(int(input('Введите значение d: ')))

print('Минимальное значение - ', min(a, b, c, d))

# Задание 2 - Вариант 11
entered_value = int(input('Введите число XXX: '))

first_number = entered_value // 100
third_number = entered_value % 10
second_number = entered_value // 10 % 10

result = first_number * 10 + third_number + second_number * 100

print('Искомое число после перестановки 1 и 2 цифр: ', result)
