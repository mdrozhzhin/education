import random

massive = [random.randint(0, 50) for _ in range(50)]
print(massive)

evens = []

for i in massive:
    if i % 2 == 0 and i < 10:
        evens.append(i)

if len(evens) == 0:
    print('No numbers')

print(sorted(evens, reverse=True))
