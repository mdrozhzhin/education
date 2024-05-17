'''
 Анонимные функции, lambda-выражения
'''

lfunc = lambda x, y, z = 1: x + y + z
print("lfunc(1,2,3): ", lfunc(1, 2, 3))
print("lfunc(1,2): ", lfunc(1, 2))
print("lfunc(x=1,y=3): ", lfunc(x=1, y=3))
print("lambda result: ", (lambda a, b, sep=", ": sep.join((a, b)))("Hello", "World!"))
print("\n")

# Лямбда-функция проверяет делимость на 3 и возвращает число, если остаток равен нулю.
lam = lambda num: print(num) if num % 3 == 0 else None

# Получаем ввод данных с клавиатуры
number = int(input("Введите число: "))
lam(number)
