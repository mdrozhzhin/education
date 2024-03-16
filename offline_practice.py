import math
import random

# Лабораторная работа №2, задание №1

a = math.cos(int(input('Введите значение a: ')))
b = math.cos(int(input('Введите значение b: ')))
c = math.cos(int(input('Введите значение c: ')))
d = math.cos(int(input('Введите значение d: ')))

print('Минимальное значение - ', min(a, b, c, d))


# Лабораторная работа №2, задание №2

entered_value = int(input('Введите число XXX: '))

first_number = entered_value // 100
third_number = entered_value % 10
second_number = entered_value // 10 % 10

result = first_number * 10 + third_number + second_number * 100

print('Искомое число после перестановки 1 и 2 цифр: ', result)


# Лабораторная работа №2, дополнительное задание

year = int(input('Введите год: '))

days = 0

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    days = 365
else:
    days = 366

print(f'В {year} году - {days} дней')


# Лабораторная работа №3, задание №1.1

set_resistance = [10, 20, 30, 40, 50]

total_resistance = 0

for i in set_resistance:
    total_resistance += i

print("Общее сопротивление цепи:", total_resistance)

# Лабораторная работа №3, задание №1.2

N = random.randint(1, 30)
print(f'Случайно сгенерированное число: {N}')

K = 1

while K**2 <= N:
    K += 1

print(f'Искомое число: {K-1}')


# Лабораторная работа №3, задание №2


def taylor_series(x, eps):
    y = 0
    n = 0
    term = 1
    while abs(term) > eps:
        y += term
        n += 1
        term *= 1 / ((2 * n + 1) * x ** (2 * n + 1))
    return y, n

def taylor_series(x, eps):
    y = 0
    n = 0
    term = 1
    while abs(term) > eps:
        y += term
        n += 1
        term *= 1 / ((2 * n + 1) * x ** (2 * n + 1))
    return y, n

def print_table(start_x, end_x, dx, eps):
    print("Таблица значений функции, заданной рядом Тейлора")
    print("===================================================")
    print("|    X    |    Y    |   Количество членов ряда   |")
    print("===================================================")
    x = start_x
    while x <= end_x:
        y, n = taylor_series(x, eps)
        print(f"|  {x:.2f}  |  {y:.6f}  |            {n}            |")
        x += dx
    print("===================================================")


start_x = float(input("Введите начальное значение X: "))
end_x = float(input("Введите конечное значение X: "))
dx = float(input("Введите шаг dx: "))
eps = float(input("Введите точность epsilon: "))

print_table(start_x, end_x, dx, eps)
