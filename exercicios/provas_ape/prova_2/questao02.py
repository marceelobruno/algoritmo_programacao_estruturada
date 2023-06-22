"""
Escreva um programa que leia uma matriz, de ordem 10 x 12,
contendo números inteiros, calcule e imprima:
a) O maior elemento da primeira linha da matriz;
b) A soma dos elementos da última coluna da matriz.
"""
import random

lin = 10
col = 12

mat = [[None] * col for i in range(lin)]

for i in range(lin):
    for j in range(col):
        mat[i][j] = random.randint(1, 50)

maior_lin = mat[0][0]
soma_col = 0

for i in range(lin):
    for j in range(col):
        if i == 0:
            if mat[i][j] > maior_lin:
                maior_lin = mat[i][j]
        if j == col - 1:
            soma_col += mat[i][j]

print('Matriz:')
for i in range(lin):
    for j in range(col):
        print(f'{mat[i][j]:4}', end=' ')
    print()

print(f'''\n
Maior elemento da 1ª linha: {maior_lin}
Soma dos elementos da última coluna: {soma_col}''')
