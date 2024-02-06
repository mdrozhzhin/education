import math

x = int(input('Enter x: '))
y = int(input('Enter y: '))

d = (2*math.cos(x - math.pi/6))/(1/2 + math.sin(y)**2) + math.fabs(y - x)/3
print(d)
