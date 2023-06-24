"""
http://www.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

1. Faça um algoritmo que construa uma matriz de nome MAT de 10 linhas e 15
colunas contendo números inteiros. Em seguida escreva a soma dos elementos de
cada linha e se a soma dos elementos é par ou ímpar.
Por fim escreva a soma dos elementos de cada coluna e se a soma dos elementos
é par ou ímpar.
"""
from random import randint

# Ordem da matriz
lin = 3
col = 5

# Criando e preenchendo a matriz usando List Comprehension
mat = [[randint(00,30) for j in range(col)] for i in range(lin)]


# Printando a matriz
print('Matriz')
for i in range(lin):
    for j in range(col):
        print(f'{mat[i][j]:4}',end=' ')
    print()
print()

# Calculando os elementos das linhas
for i in range(lin):
    soma_lin = 0
    for j in range(col):
        soma_lin += mat[i][j]
    print(f'Soma dos elementos da {i+1}ª linha: {soma_lin}.',end=' ')
    if soma_lin %2==0:
        print('Resultado é par.')
    else:
        print('Resultado é ímpar.')
print()

# Calculando os elementos das colunas
for j in range(col):
    soma_col = 0
    for i in range(lin):
        soma_col += mat[i][j]
    print(f'Soma dos elementos da {j+1}ª coluna: {soma_col}.',end=' ')
    if soma_col %2==0:
        print('Resultado é par.')
    else:
        print('Resultado é ímpar.')
