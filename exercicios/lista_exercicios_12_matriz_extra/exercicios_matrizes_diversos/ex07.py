"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

5. Faça um programa que leia a dimensão de uma matriz (de números inteiros) M e N,
onde M é o número de linhas e N é o número de colunas. A seguir, leia os elementos
da matriz, e calcule e exiba a soma dos elementos da coluna onde se encontra o maior
elemento da matriz.
"""

# ordem da matriz
m = int(input('Número de linhas: '))
n = int(input('Número de colunas: '))

# gerando a matriz
mat = [[None]*n for i in range(m)]

# variáveias auxiliares
soma = 0
maior = 0
index_maior = 0

# preenchendo a matriz
print('\nInforme os elementos da matriz:')
for i in range(m):
    for j in range(n):
        mat[i][j] = int(input())
        if mat[i][j] > maior:
            maior = mat[i][j]
            index_maior = j

# somando a coluna que contém o maior elemento
for j in range(n):
    for i in range(m):
        if j == index_maior:
            soma += mat[i][j]

# imprimindo a matriz
print('\nMatriz:')
for i in range(m):
    for j in range(n):
        print(f'{mat[i][j]:4}',end=' ')
    print()

print(f'''
\nMaior elemento: {maior}
Soma da coluna que possui o maior elemento: {soma}.''')
