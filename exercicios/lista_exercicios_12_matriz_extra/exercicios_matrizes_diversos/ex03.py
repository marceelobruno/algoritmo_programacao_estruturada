"""
https://www.galirows.com.br/meublog/programacao/exercicios-simples-com-matrizes/

Algoritmo 3 - Dada uma matriz A(mxn), imprima o número de linhas e o
número de colunas nulas da matriz.
"""
import random

# Ordem da matriz
lin = 2
col = 3

cont_lin = 0
cont_col = 0

# Gerando a matriz
mat = [[None] * col for i in range(lin)]

# Preenchendo e imprimindo a matriz
print('Matriz')
for i in range(lin):
    for j in range(col):
        mat[i][j] = random.randint(0,1)
        print(f'{mat[i][j]:4}', end=' ')
    print()

# Calculando número de linhas nulas
for i in range(lin):
    zeros = 0
    for j in range(col):
        if mat[i][j] == 0:
            zeros += 1
    if zeros == col:
        cont_lin += 1
print(f'\nNúmero de linhas nulas: {cont_lin}')

# Calculando número de colunas nulas
for j in range(col):  # fixando as colunas
    zeros = 0
    for i in range(lin):  # variando as linhas
        if mat[i][j] == 0:  # se encontrar um 0 incrementa na variável 'zeros'
            zeros += 1
    if zeros == lin:  # testando se o número de 0 é o mesmo que o número de linhas
        cont_col += 1
print(f'Número de colunas nulas: {cont_col}')
