"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

6. Faça um programa que leia a dimensão de uma matriz de inteiros M e N, onde M é
o número de linhas e N é o número de colunas. A seguir, leia os elementos da matriz,
conte e escreva quantos valores maiores que 10 ela possui.
"""
from random import randint

m = int(input('Informe o número de linhas: '))
n = int(input('Informe o número de colunas: '))

mat = [[None]*n for i in range(m)]

cont = 0

print('Informe os elementos da matriz:')
for i in range(m):
    for j in range(n):
        mat[i][j] = randint(1,30)
        if mat[i][j] > 10:
            cont += 1

print('\nMatriz:')
for i in range(m):
    for j in range(n):
        print(f'{mat[i][j]:4}',end=' ')
    print()

print(f'\nQuantidade de elementos maiores que 10: {cont}.')
