"""
6. Leia duas matrizes 4 x 4 e escreva uma terceira com
os maiores valores de cada posição das matrizes lidas.
"""
from random import randint

n = 4
a = [[None]*n for i in range(n)]
b = [[None]*n for i in range(n)]
c = [[None]*n for i in range(n)]

print('Matriz A:')
for i in range(n):
    for j in range(n):
        a[i][j] = randint(1,50)
        print(f'{a[i][j]:4}',end='')
    print()

print('\nMatriz B:')
for i in range(n):
    for j in range(n):
        b[i][j] = randint(1,50)
        print(f'{b[i][j]:4}',end='')
    print()

print('\nMatriz C:')
for i in range(n):
    for j in range(n):
        if a[i][j] >= b[i][j]:
            c[i][j] = a[i][j]
        else:
            c[i][j] = b[i][j]
        print(f'{c[i][j]:4}',end='')
    print()
