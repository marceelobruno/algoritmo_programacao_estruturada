"""
Escreva um programa que leia 2 vetores (A e B) com 5 elementos cada e gere um
terceiro vetor de 10 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores, dessa vez (B e A).
Ao final o programa deverá mostrar os dois vetores originais e o
terceiro vetor com os valores intercalados.
Exemplo: A = [18, 12, 20], B = [15, 10, 7], C = [15, 18, 10, 12, 7, 20]
"""
# ruff: noqa: E501
from random import randint

tam = 5
a = []
b = []
c = []

print(f'Informe {tam} elementos para o vetor A:')
while len(a) < tam:
    num_a = randint(1,10)
    a.append(num_a)
print('A =', a)

print(f'\nInforme {tam} elementos para o vetor B:')
while len(b) < tam:
    num_b = randint(10,20)
    b.append(num_b)
print('B =', b)

# Intercalando os vetores para gerar o vetor C
print('\nVetor C:',)
for i in range(tam):
    c.append(b[i])
    c.append(a[i])
print('C =', c)
