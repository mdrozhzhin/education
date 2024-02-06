import random

set_resistance = [10, 20, 30, 40, 50]

total_resistance = 0

for i in set_resistance:
    total_resistance += i

print("Общее сопротивление цепи:", total_resistance)


N = random.randint(1, 30)
print(f'Случайно сгенерированное число: {N}')

K = 1

while K**2 <= N:
    K += 1

print(f'Искомое число: {K-1}')
