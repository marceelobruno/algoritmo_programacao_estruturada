"""
http://profs.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

Faça um algoritmo que construa uma matriz de nome MAT de 10 linhas e 15 colunas
contendo números inteiros. Em seguida escreva a soma dos elementos de cada linha
e se a soma dos elementos é par ou impar. Por fim escreva a soma dos elementos de
cada coluna e se a soma dos elementos é par ou impar.
"""
import random

# ordem da matriz
lin = 10
col = 15

# criando a matriz
MAT = [[None]*col for i in range(lin)]

# preenchendo e imprimindo a matriz
print('Matriz:')
for i in range(lin):
    for j in range(col):
        MAT[i][j] = random.randint(1,100)
        print(f'{MAT[i][j]:4}',end=' ')
    print()
print()

# calculando as linhas
for i in range(lin):
    soma_lin = 0
    for j in range(col):
        soma_lin += MAT[i][j]
    print(f'Soma da {i+1}ª linha: {soma_lin}')
print()

# calculando as colunas
for j in range(col):
    soma_col = 0
    for i in range(lin):
        soma_col += MAT[i][j]
    print(f'Soma da {j+1}ª coluna: {soma_col}')
print()
