"""
Gerar uma matriz (3 x 5) com valores inteiros aleatórios (entre 1 e 10),
calcular a soma de cada linha e a soma de cada coluna.
"""
from random import randint

# Inicializando os valores da matriz
nlin = 3 # linhas
ncol = 5 # colunas

# Criando a matriz com valores nulos
matriz = [[None]*ncol for i in range(nlin)]

# Preenchendo a matriz com valores entre 1-10
for i in range(nlin):
    for j in range(ncol):
        matriz[i][j] = randint(1,10)

# Impressão da matriz
print('\nMatriz:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{matriz[i][j]:4}',end=' ')
    print()

# Somando linhas
print('\nSomando cada linha:')
for i in range(nlin):
    somaLin = 0
    for j in range(ncol):
        somaLin += matriz[i][j]
    print(f'{somaLin:4}',end=' ')

# Somando colunas
print('\nSomando as colunas:')
for j in range(ncol):
    somaCol = 0
    for i in range(nlin):
        somaCol += matriz[i][j]
    print(f'{somaCol:4}',end=' ')
