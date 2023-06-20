"""
4. Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de
uma dada matriz. Assim, dada uma matriz C de ordem m x n, a matriz transposta dela
será representada por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].

Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
pelo usuário (ou gerados aleatoriamente) e gere a sua transposta.
Ao final, imprima as duas matrizes (no formato de matriz).
"""
import random

m = 3 # Linhas
n = 5 # Colunas

# Criação das matrizes
a = [[None]*n for i in range(m)]
b = [[None]*m for i in range(n)]

# Gerando valores para matriz A
print('Matriz A:')
for i in range(m):
    for j in range(n):
        a[i][j] = random.randint(1,30)
        print(f'{a[i][j]:4}',end=' ')
    print()

# Gerando matriz transposta
for i in range(m):
    for j in range(n):
        b[j][i] = a[i][j]

# Imprimindo Matriz Transposta
print('\nMatriz Transposta:')
for i in range(n):
    for j in range(m):
        print(f'{b[i][j]:4}',end=' ')
    print()
