import numpy as np


def counting_rows(matrix, threshold):
    count = 0
    for row in matrix:
        if np.mean(row) < threshold:
            count += 1
    return count


def find_divisible_elements(matrix):
    num_columns = len(matrix[0])
    result = []
    for j in range(num_columns):
        column_elements = [row[j] for row in matrix]
        divisible_elements = [element for element in column_elements if is_divisible(element, j+1)]
        if divisible_elements:
            result.append((j+1, divisible_elements))
    return result


def is_divisible(number, divisor):
    divisors = [i for i in range(1, number+1) if number % i == 0]
    return any(divisor % i == 0 for i in divisors)


matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

C = int(input('Введите искомое среднеарифметическое: '))

count_rows = counting_rows(matrix, C)
print("Количество строк, среднеарифметическое элементов которых меньше {}: {}".format(C, count_rows))

divisible_elements = find_divisible_elements(matrix)

if divisible_elements:
    for column, elements in divisible_elements:
        print("В столбце {} найдены элементы: {}".format(column, elements))
else:
    print("В каждом столбце не найдено элементов, у которых произведение делителей кратно номеру столбца.")
