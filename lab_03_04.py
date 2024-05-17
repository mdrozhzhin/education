'''
 Словари
'''

d1 = {
 "day": 18,
 "month": 6,
 "year": 1983
}

d2 = dict(bananas=3,apples=5,oranges=2,bag="basket")
d3 = dict([("street","Kronverksky pr."), ("house",49)])
d4 = dict.fromkeys(["1","2"], 3)

print("Dict d1 = ", d1)
print("Dict d2 by dict()= ", d2)
print("Dict d3 by dict([])= ", d3)
print("Dict d4 by fromkeys = ", d4)
print("\n")

# Создание словаря startDict с ключами 'ready', 'set', 'go' и значениями 3, 2, 1
startDict1 = {'ready': 3, 'set': 2, 'go': 1}
startDict2 = dict(ready=3, set=2, go=1)
startDict3 = dict([('ready', 3), ('set', 2), ('go', 1)])

# Вывод созданных словарей на экран
print("Dictionary startDict1:", startDict1)
print("Dictionary startDict2:", startDict2)
print("Dictionary startDict3:", startDict3)

# Создание словаря dict1 с ключами 'key1' и 'key2', значения которых вводятся с клавиатуры
value_input = input("Введите значение для ключей 'key1' и 'key2': ")

dict1 = {'key1': value_input, 'key2': value_input}

# Вывод созданного словаря dict1 на экран
print("Dictionary dict1:", dict1)

