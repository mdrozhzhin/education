import math

h = False
f = 0

while h == False:
    y = int(input('Enter y: '))
    x = int(input('Enter x: '))
    z = int(input('Enter z: '))
    if z + x ** 2 / 4 != 0 and x ** 2 / 4 != 0:
        f = math.log(math.fabs((y - math.sqrt(math.fabs(x))) * (x - y / (z + x ** 2 / 4))))
        h = True
        print(f)
    else:
        print('Делить на 0 нельзя! Введите корректные значения!')
        h = False

#Enter y: 2
#Enter x: 3
#Enter z: 4
#-0.33114110240205097