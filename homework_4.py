import math

x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))

b = (3 + math.e**(y - 1)) / (1 + x**2 * math.fabs(y - math.tan(z)))
print(b)
