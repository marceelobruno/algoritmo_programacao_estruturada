"""
4. Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de
uma dada matriz. Assim, dada uma matriz C de ordem m x n, a matriz transposta dela
será representada por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].

Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
pelo usuário (ou gerados aleatoriamente) e gere a sua transposta.
Ao final, imprima as duas matrizes (no formato de matriz).
"""
import random

lin = 3 # Linhas
col = 5 # Colunas

# Criação das linatrizes
a = [[(random.randint(1,30))for j in range(col)] for i in range(lin)]
b = [[None]*lin for i in range(col)]

# Gerando valores para matriz A
print('Matriz A:')
for i in range(lin):
    for j in range(col):
        # a[i][j] = random.randint(1,30)
        print(f'{a[i][j]:4}',end=' ')
    print()

# Gerando matriz transposta
for i in range(lin):
    for j in range(col):
        b[j][i] = a[i][j]

# Imprimindo Matriz Transposta
print('\nMatriz Transposta:')
for i in range(col):
    for j in range(lin):
        print(f'{b[i][j]:4}',end=' ')
    print()
