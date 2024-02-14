# Определяем пустые списки.
list_of_numbers = []
list_of_even = []

# Генерируем список
for i in range(10):
    list_of_numbers.append(i)

# Проходимся циклом по списку и добавляем все значения, которые делятся на 2 без остатка, в лист.
for i in list_of_numbers:
    if i % 2 == 0:
        list_of_even.append(i)
        print(i)
    else:
        pass

# Используя функцию max находим наибольшее значение элемента списка.
print(max(list_of_even))
