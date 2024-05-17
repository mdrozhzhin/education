'''
 Аргументы функции
'''


def sum(x, y, z=1):
    return x + y + z


print("sum(1,2,3): ", sum(1, 2, 3))
print("sum(1,2): ", sum(1, 2))
print("sum(x=1,y=3): ", sum(x=1, y=3))

# переменное количество аргументов
def printArgs(*args):
    print("args of printArgs(): ", args)
    return


# переменное количество аргументов и аргументовключевых слов
def printArgsnKwargs(m, *args, **kwargs):
    print("main argument of printArgsnKwargs(): ", m)
    print("args of printArgsnKwargs(): ", args)
    print("args of printArgsnKwargs(): ", kwargs)
    return


printArgs("Hello World!", 1, 3, 5)
printArgsnKwargs("Earth", 7.125, radius=6371, pos=3)
print("\n")


# Определение функции checkArgs с переменным количеством аргументов и аргументов-ключевых слов
def checkArgs(*args, **kwargs):
    # Получаем количество переданных позиционных аргументов (args) и аргументов-ключевых слов (kwargs)
    num_positional_args = len(args)
    num_keyword_args = len(kwargs)

    # Проверяем условия
    if num_positional_args <= 3 and num_keyword_args < 3:
        # Выводим переданные аргументы на экран
        print("Переданные позиционные аргументы:", args)
        print("Переданные аргументы-ключевые слова:", kwargs)
    else:
        # Выводим предупреждение о превышении количества аргументов
        print("Предупреждение: Превышено количество передаваемых аргументов!")


# Вызов функции checkArgs с разным количеством аргументов
checkArgs(1, 2, 3, a='apple', b='banana')  # Выведет аргументы на экран
checkArgs(10, 'hello', x=100, y=200, z=300)  # Выведет предупреждение о превышении количества аргументов
