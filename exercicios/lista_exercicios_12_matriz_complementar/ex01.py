"""
3. Escreva um programa que preencha uma matriz quadrada de ordem 3 com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente),
calcule e exiba:
    i. A soma dos elementos de cada linha;
    ii. A soma dos elementos de cada coluna;
    iii. A soma dos elementos da diagonal principal da matriz;
    iv. A soma dos elementos da diagonal secundária da matriz;
    v. A soma de todos os elementos da matriz.
"""
import random  # Geração aleatória dos elementos da matriz

# Ordem da matriz quadrada
n = 3

# Criação da matriz
m = [[None] * n for i in range(n)]

# Leitura da matriz
"""
print('\nDigite os elementos da matriz:')
for i in range(n):
    for j in range(n):
        m[i][j] = int(input(f'M[{i}][{j}]: '))
"""


for i in range(n):
    for j in range(n):
        m[i][j] = random.randint(1, 10)

# Exibição da matriz
print('\nMatriz:')
for i in range(n):
    for j in range(n):
        print(f'{m[i][j]:4}', end='')
    print()

# Soma das linhas
print('\nSoma de cada linha:')
for i in range(n):
    s = 0
    for j in range(n):
        s += m[i][j]
    print(f'{s:4}')

# Soma das colunas
print('\nSoma de cada coluna:')
for j in range(n):
    s = 0
    for i in range(n):
        s += m[i][j]
    print(f'{s:4}', end='')

# Soma da diagonal principal
print('\n\nSoma da diagonal principal:')
s = 0
for i in range(n):
    for j in range(n):
        if i == j:
            s += m[i][j]
print(f'{s:4}')

# Outra forma para a soma da diagonal principal
'''
print('\n\nSoma da diagonal principal:')
s = 0
for i in range(n):
    s += m[i][i]
print(f'{s:4}')
'''

# Soma da diagonal secundária
print('\nSoma da diagonal secundária:')
s = 0
for i in range(n):
    for j in range(n):
        if i + j == n - 1:  # outra condição possível:  i == n-j-1
            s += m[i][j]
print(f'{s:4}')

# Outra forma para a soma da diagonal secundária
'''
print('\nSoma da diagonal secundária:')
s = 0
for i in range(n):
    s += m[i][n-i-1]
print(f'{s:4}')
'''

# Soma de toda a matriz
print('\nSoma de toda a matriz:')
s = 0
for i in range(n):
    for j in range(n):
        s += m[i][j]
print(f'{s:4}')
