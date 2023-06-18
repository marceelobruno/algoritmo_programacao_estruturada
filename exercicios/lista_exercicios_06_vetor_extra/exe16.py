"""
21. Faça um programa que receba do usuário dois vetores, A e B,
com 10 números inteiros cada.
Crie um novo vetor denominado C calculando C = A - B.
Mostre na tela os dados do vetor C.
"""
from random import randint

tam = 10
a = [None] * tam
b = [None] * tam
c = [None] * tam

print('Informe valores para os vetores A e B:')
for i in range(tam):
    print(f'Informe o {i+1}° valor para A: ')
    a[i] = randint(11, 20)
    print(f'Informe o {i+1}° valor para B: ')
    b[i] = randint(1, 10)
    c[i] = a[i] - b[i]
    print()

print('Vetor A =', a)
print('Vetor B =', b)
print('Resultado da subtração entre A e B =', c)
