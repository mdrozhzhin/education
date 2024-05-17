'''
 Операции cо словарями
'''
d2 = dict(bananas=3,apples=5,oranges=2,bag="basket")
d5 = d2.copy() # создание копии словаря
print("Dict d5 copying d2 = ", d5)

# получение значения по ключу
print("Get dict value by key d5['bag']: ", d5["bag"])
print("Get dict value by key d5.get('bag'): ", d5.get('bag'))
print("Get dict keys d5.keys(): ", d5.keys()) # список ключей
print("Get dict values d5.values(): ", d5.values()) # список значений
print("\n")

# Создание словаря myInfo с информацией о персональных данных
myInfo = {
    "surname": "Фамилия",
    "name": "Имя",
    "middlename": "Отчество",
    "day": 1,
    "month": "Январь",
    "year": 2000,
    "university": "Мой университет"
}

# Получение и вывод списка ключей словаря myInfo
keys_list = list(myInfo.keys())
print("Список ключей словаря myInfo:", keys_list)

# Получение и вывод списка значений словаря myInfo
values_list = list(myInfo.values())
print("Список значений словаря myInfo:", values_list)