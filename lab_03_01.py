'''
 Кортежи
'''

# создание кортежа
a1 = tuple()
a2 = 1, 2, 3, "abc"
a3 = (1, 2, 3, "abc")
print("Tuple a1 = ", a1)
print("Tuple a2 = ", a2)
print("Tuple a3 = ", a3)

# создание кортежа из других структур данных
l = [1, 2, 3, "abc"] # из списка
a4 = tuple(l)
print("Tuple a4 from list l = ", a4)
a5 = tuple("Hello, World!") # из строки
print("Tuple a5 from string = ", a5)

# вложенность кортежей
a6 = a2, a3
print("Tuple a6 formed by a2 and a3 = ", a6)

# объединение кортежей
a7 = a2 + a3
print("Tuple a7 by combining a2 and a3 = ", a7)

# доступ к элементам кортежей
print("a6[0]: ", a6[0])
print("a6[0][3]: ", a6[0][3])

#a6[0][3] = "cba"
print("\n")

# Ввод данных для кортежа 1
day = input('Введите день рождения: ')
month = input('Введите месяц рождения: ')
year = input('Введите год рождения: ')

k1 = (day, month, year)

# Ввод данных для кортежа 2
surname = input('Введите фамилию: ')
name = input('Введите имя: ')
patronymic = input('Введите отчество: ')

k2 = (surname, name, patronymic)

# Объединим кортежи
k3 = k1 + k2

print(f'Объединённый кортеж: {k3}')

# создание кортежа k4, в котором вложены кортежи k1 и k2
k4 = (k1, k2)

# вывод значения переменной k4 на экран
print("Вложенный кортеж k4: ", k4)

# вывод второго элемента второго вложенного кортежа (элемент 'name' из k2)
print("Второй элемент второго вложенного кортежа k4: ", k4[1][1])