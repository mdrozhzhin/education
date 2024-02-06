import math

x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))

w = ((x / y) * (z + x) * math.e**math.fabs(x - y) + math.log(1 + math.e)) / (math.sin(y)**2 - (math.sin(x) * math.sin(y))**2)
print(w)
