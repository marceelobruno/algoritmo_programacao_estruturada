"""
3. Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor.
Se estiver, informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
aparece.
"""
from random import randint

n = int(input('Informe o tamanho do vetor V: '))
v = [None] * n

print('Informe os elementos do vetor V: ')
for i in range(n):
    v[i] = randint(1, 10)

print('V = ', v)
k = int(input('Digite o valor de K: '))

existe = False
for e in v:
    if e == k:
        existe = True
        break

if existe:
    print(f'\nO valor {k} encontra-se nos seguintes índices:', end=' ')
    for i in range(n):
        if v[i] == k:
            print(i, end=' ')

else:
    print(f'O valor {k} não encontra-se no vetor.')
