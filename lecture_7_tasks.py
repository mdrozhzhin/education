#A = [[0] * 3] * 3
#print(A)
#A[0][0] = 1
#print(A)

A = [0] * 3

for i in range(3):
    A[i] = [0] * 3

print(f'A = {A}')

B = []

for i in range(3):
    B.append([0] * 4)
print(f'B = {B}')

n = 3
C = []

for i in range(n):
    D = []
    for i in range(n):
        D.append(int(input()))
    C.append(D)
print(f'C = {C}')

for i in range(n):
    for j in range(n):
        print(C[i][j], end = ' ')
    print()

for row in C:
    for elem in row:
        print(elem, end =' ')
    print()

for row in C:
    print(''.join(list(map(str, row))))
