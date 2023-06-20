"""
1. Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3,
com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente).
O programa deverá somar as duas matrizes, armazenando o resultado em uma
terceira matriz (C). Ao final, exiba as 3 matrizes (no formato de matriz).
"""
from random import randint

# Inicializando os valores das matrizes
lin = 2 # número de linhas da matriz
col = 3 # número de colunas da matriz

# Gerando as matrizes
a = [[None] * col for i in range(lin)]
b = [[None] * col for i in range(lin)]
c = [[None] * col for i in range(lin)]

# Fornecendo valores aleatórios para matriz A entre 1-20
for i in range(lin):
    for j in range(col):
        a[i][j] = randint(1, 20)

# Fornecendo valores aleatórios para matriz B entre 1-20
for i in range(lin):
    for j in range(col):
        b[i][j] = randint(1, 20)

# Gerando a matriz C através dos resultados das matrizes A + B
for i in range(lin):
    for j in range(col):
        c[i][j] = a[i][j] + b[i][j]

# Imprimindo as matrizes A, B e C
print('\nMatriz A:')
for i in range(lin):
    for j in range(col):
        print(f'{a[i][j]:4}', end=' ')
    print()

print('\nMatriz B:')
for i in range(lin):
    for j in range(col):
        print(f'{b[i][j]:4}', end=' ')
    print()

print('\nMatriz C:')
for i in range(lin):
    for j in range(col):
        print(f'{c[i][j]:4}', end=' ')
    print()
