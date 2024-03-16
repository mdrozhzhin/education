import random


def modify_element(arr, k):
    if k >= len(arr):
        print("Ошибка: индекс k превышает размер массива")
        return arr
    else:
        last_element = arr[-1]
        arr[k] *= last_element
        return arr


array = [random.randint(1, 20) for i in range(10)]
k_index = 2
modified_array = modify_element(array, k_index)
print("Измененный массив:", modified_array)


def multiply_numbers(arr):
    product = 1
    for i in range(len(arr)):
        if i > 2 * i or i % 2 == 0:
            product *= arr[i]
    return product


array = [random.randint(1, 10) for c in range(10)]
result = multiply_numbers(array)
print("Произведение элементов соответствующих условиям:", result)


def calculate_precipitation_decades(arr):
    decades_of_month = [0, 0, 0]
    for i in range(len(arr)):
        decade_index = i // 10
        if decade_index < len(decades_of_month):
            decades_of_month[decade_index] += arr[i]
    return decades_of_month


month_precipitation = [random.randint(0, 100) for v in range(0, 31)]

decades_of_month = calculate_precipitation_decades(month_precipitation)
print("Количество осадков за каждую декаду июня:", decades_of_month)


def min_absolute_value_index(arr):
    min_abs_index = None
    min_abs_value = float('inf')
    for i in range(len(arr)):
        abs_value = abs(arr[i])
        if abs_value < min_abs_value:
            min_abs_value = abs_value
            min_abs_index = i
    return min_abs_index


array = [3, -5, 2.5, -1.5, 4]
index = min_absolute_value_index(array)
print("Номер минимального по модулю элемента:", index)


def sum_after_first_negative(arr):
    found_negative = False
    sum_after_negative = 0
    for i in range(len(arr)):
        if found_negative:
            sum_after_negative += abs(arr[i])
        elif arr[i] < 0:
            found_negative = True
    return sum_after_negative


array = [3, -5, 2.5, -1.5, 4]
result = sum_after_first_negative(array)
print("Сумма модулей элементов после первого отрицательного элемента:", result)


def compress_array(arr, a, b):
    compressed_array = [x for x in arr if x < a or x > b]
    compressed_array.extend([0] * (len(arr) - len(compressed_array)))
    return compressed_array


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_value = 3
b_value = 7
compressed_result = compress_array(array, a_value, b_value)
print("Сжатый массив:", compressed_result)


def process_array(arr, a=None, b=None):
    if not arr:
        print("Массив пуст")
        return None

    min_abs_index = None
    min_abs_value = float('inf')
    for i in range(len(arr)):
        abs_value = abs(arr[i])
        if abs_value < min_abs_value:
            min_abs_value = abs_value
            min_abs_index = i

    found_negative = False
    sum_after_negative = 0
    for i in range(len(arr)):
        if found_negative:
            sum_after_negative += abs(arr[i])
        elif arr[i] < 0:
            found_negative = True

    if a is not None and b is not None:
        arr = [x for x in arr if x < a or x > b]
        arr.extend([0] * (len(arr) - len(arr)))

    return min_abs_index, sum_after_negative, arr


array = [3, -5, 2.5, -1.5, 4]
a_value = 1
b_value = 3
result = process_array(array, a_value, b_value)
print("Номер минимального по модулю элемента:", result[0])
print("Сумма модулей элементов после первого отрицательного элемента:", result[1])
print("Сжатый массив:", result[2])
