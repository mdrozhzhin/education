import math

perimeter = 84
hypotenuse = 37

# perimeter == a + b + c or 84 == a + b + 37
# 37**2 == a + b + 37
# a = 84 - b - 37
# 37**2 == (84 - b - 37)**2 + b**2
# 2b**2 - 94b + 840 = 0

# Коэффициенты квадратного уравнения
a = 2
b = -94
c = 840

# Решение уравнения
discriminant = math.sqrt(b**2 - 4*a*c)

root1 = int((-b + discriminant) / (2*a))
root2 = int((-b - discriminant) / (2*a))

# Берем только положительный корень
leg_b = max(root1, root2).real

print(f"Leg b is equal: {leg_b}")

leg_a = 84 - leg_b - 37
print(f"Leg a is equal: {leg_a}")

triangle_square = (leg_a * leg_b)*0.5
print(f"Triangle's square is equal: {triangle_square}")
