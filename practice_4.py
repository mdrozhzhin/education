l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [3, 4, 5, 6, 7, 8, 9 ,10]
l3 = [5, 6, 7, 8, 9, 10, 11, 12]

l4 = l1 + l2 + l3

l5 = l1
l5[0] = 12

print(l5)
print(l1)

l6 = []
for i in l1:
    l6.append(i % 2)
print(l6)