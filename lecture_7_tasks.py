import random

matrix_size = int(input('Какого размера матрицу Вы хотите использовать?'))
quad_matrix = []


def quad_matrix_generatror():
    if matrix_size <= 0:
        return None

    unique_numbers = list(range(1, matrix_size ** 2 + 1))

    random.shuffle(unique_numbers)

    for i in range(matrix_size):
        row = unique_numbers[i * matrix_size:(i + 1) * matrix_size]
        quad_matrix.append(row)

    return quad_matrix


matrix = quad_matrix_generatror()


def matrix_print():
    for row in range(matrix_size):
        for elem in range(matrix_size):
            print(matrix[row][elem], end=' ')
        print()


matrix_print()


def seeking_row_with_min_value(matrix):
    min_row_sum = float('inf')
    min_row_index = -1

    for i, row in enumerate(matrix):
        row_sum = sum(row)
        if row_sum < min_row_sum:
            min_row_sum = row_sum
            min_row_index = i

    return min_row_index


min_row_index = seeking_row_with_min_value(matrix)
print("Индекс строки с минимальной суммой элементов:", min_row_index)


def seeking_column_with_min_product(matrix):
    min_product = float('inf')
    min_column_index = -1

    for j in range(len(matrix[0])):
        product = 1
        for i in range(len(matrix)):
            if abs(matrix[i][j]) <= 10:
                product *= matrix[i][j]
            else:
                product = float('inf')
                break
        if product < min_product:
            min_product = product
            min_column_index = j

    return min_column_index


min_column_index = seeking_column_with_min_product(matrix)

if min_column_index != -1:
    adjacent_column_index = min_column_index + 1 if min_column_index < len(matrix[0]) - 1 else min_column_index - 1
    matrix = [list(row) for row in zip(*matrix)]
    matrix[min_column_index], matrix[adjacent_column_index] = matrix[adjacent_column_index], matrix[min_column_index]
    matrix = [list(row) for row in zip(*matrix)]  # Транспонируем обратно

    print("Индекс столбца с минимальным произведением элементов:", min_column_index)
    print("Матрица с поменяными местами столбцами:")
    for row in matrix:
        print(row)
else:
    print("Нет столбцов, удовлетворяющих условию.")
