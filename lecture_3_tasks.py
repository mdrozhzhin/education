import math

# Task 1

status = True

while status == True:
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    z = int(input('Enter z: '))

    if (math.sin(y)**2 - (math.sin(x) * math.sin(y))**2) != 0:
        w = ((x / y) * (z + x) * math.e**math.fabs(x - y) + math.log(1 + math.e)) / (math.sin(y)**2 - (math.sin(x) * math.sin(y))**2)
        print(w)
        status = False
    else:
        print(f'Знаменатель равен нулю. Деление на ноль недопустимо. Введите другие значения.')
        status = True


# Task 2

status_2 = True

x = int(input('Введите x: '))
y = int(input('Введите y: '))

if y != 0 and x / y > 0:
    b = math.log(x / y) + (x**2 + y)**3
    print(f'b = {b}')
elif y != 0 and x / y < 0:
    b = math.log(math.fabs(x / y)) + (x**2 + y)**3
    print(f'b = {b}')
elif x == 0 and y != 0:
    b = (x**2 + y)**3
    print(f'b = {b}')
elif y == 0:
    b = 0
    print(f'b = {b}')
else:
    pass
