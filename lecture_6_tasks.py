import random

print(f'Задание №1. Вариант 11.')

# Определяем списки.
list_of_numbers = [random.randint(1, 20) for _ in range(1, 10)]
list_of_even = []

# Проходимся циклом по списку и добавляем все четные значения в лист.
for i in list_of_numbers:
    if i % 2 == 0:
        list_of_even.append(i)
    else:
        pass

# Используя функцию max находим наибольшее значение элемента списка.
print(f'Полученный список чётных чисел: {list_of_even}.')
print(f'Наибольший элемент списка: {max(list_of_even)}.\n')


print(f'Задание №2. Вариант 11.')

randomized_list = [random.randint(1, 20) for _ in range(1, 20)]
print(f'Случайно сгенерированный массив целых чисел: {randomized_list}.')

even_numbers = []

for i in randomized_list:
    if i % 2 == 0 and i < 10:
        even_numbers.append(i)
    else:
        pass

if len(even_numbers) == 0:
    print(f'Массив пустой.')
else:
    even_numbers.sort()
    print(f'Полученный массив: {even_numbers}.')
