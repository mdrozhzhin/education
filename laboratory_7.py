import math


def biggest_value(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return 'Введённые значения равны. Введите различные значения.'


#result = biggest_value(1, 3)
#print(f'{result}')


def volume_calc(h, r):
    return (1 / 3) * h * math.pi * (r ** 2)


#volume_of_figure1 = volume_calc(5, 3)
#volume_of_figure2 = volume_calc(3, 2)
#print(f'Объём первой фигуры равен: {volume_of_figure1}.')
#print(f'Объём второй фигуры равен: {volume_of_figure2}.')


def term_of_series(n):
    if n == 1:
        return 3
    else:
        return term_of_series(n - 1) + 0.3


n = 6
result = term_of_series(n)
print(f"{n} член порядка равен: {result:0.2f}")
