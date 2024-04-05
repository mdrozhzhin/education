import math


def max_value(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        print('Ops. Entered values equal each other.')


result = max_value(2, 1)
print(f'The biggest value is {result}.')


def volume_calc(h, r):
    return (1 / 3) * h * math.pi * (r ** 2)


volume_of_figure1 = volume_calc(5, 3)
volume_of_figure2 = volume_calc(3, 2)
print(f'The volume of 1st figure is: {volume_of_figure1}.\nThe volume of 2nd figure is: {volume_of_figure2}')


def nth_term_of_series(n):
    if n == 1:
        return 3
    else:
        return nth_term_of_series(n - 1) + 0.3


n = 6
result = nth_term_of_series(n)
print(f"The {n}-th term of the series is: {result}")
