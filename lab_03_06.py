'''
 Функции
'''


def dictUpdate(a):
    a.update([("x", 5)])
    print("dict in function: ", a)
    return


def dictNoUpdate(a):
    a = a.copy()
    a.update([("y", 3)])
    print("dict in function: ", a)
    return


def returnFunc(a):
    def f1(a):
        print("returned f1(a): ", a)
    return f1


d = {"v": 7}
dictUpdate(d)
print("dict out of function: ", d)
dictNoUpdate(d)
print("dict out of function: ", d)
f = returnFunc(d)
print("f: ", f)
f(2)
print("\n")


def returnMod():
    def calculate_mod(x):
        result = x % 15
        print("Остаток от деления {0} на 15: {1}".format(x, result))

    return calculate_mod  # Возвращаем функцию calculate_mod


# Вызов функции returnMod для получения вложенной функции
mod_func = returnMod()

# Вызов полученной функции mod_func и сохранение результата в переменную mod15
mod15 = mod_func(100)  # Выполнение расчета остатка от деления числа 100 на 15

# Вывод значения переменной mod15 (которая равна None, т.к. calculate_mod не возвращает ничего,
# а функция mod_func не имеет ничего
