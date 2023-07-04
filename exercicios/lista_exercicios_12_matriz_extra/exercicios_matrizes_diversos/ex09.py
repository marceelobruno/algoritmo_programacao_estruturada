"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

7. Faça um programa que leia a dimensão de uma matriz (de números inteiros)
quadrada N. A seguir, leia os elementos da matriz.
Faça um programa que verifique se essa matriz é diagonal.
"""

# ordem da matriz
tam = 2

# gerando a matriz
mat = [[None] * tam for i in range(tam)]

# variável para verificar se a matriz é diagonal
diagonal = True

# preenchendo a matriz
print('Informe os elementos da matriz:')
for i in range(tam):
    for j in range(tam):
        mat[i][j] = int(input())

# exibindo a matriz
print('\nMatriz:')
for i in range(tam):
    for j in range(tam):
        print(f'{mat[i][j]:4}', end=' ')
    print()

# verificando se a matriz é diagonal
for i in range(tam):
    for j in range(tam):
        if i != j and mat[i][j] != 0:
            diagonal = False
            break

if diagonal:
    print('\nMatriz é diagonal')
else:
    print('\nMatriz não é diagonal')
