"""
https://www.facom.ufu.br/~backes/gci007/ListaC04.pdf
1. Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""
import random

n = 4  # ordem da matriz

mat = [[None] * n for i in range(n)]
cont = 0
for i in range(n):
    for j in range(n):
        mat[i][j] = random.randint(1, 15)
        if mat[i][j] > 10:
            cont += 1

print('Matriz:')
for i in range(n):
    for j in range(n):
        print(f'{mat[i][j]:4}',end=' ')
    print()

if cont > 0:
    print('\nQuantidade de elementos > 10:',cont)

print()
print(mat[0][0])
print(mat[-1][-1])
