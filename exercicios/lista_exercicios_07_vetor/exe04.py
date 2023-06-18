"""
Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.
"""
from random import randint

tam = 6
a = [None]*tam

print('Informe os elementos do vetor A: ')
for e in range(tam):
    a[e] = randint(1,10)
print('A = ',a)

# Exibindo os elementos dos índices pares
print('Elementos nos índices pares:', end=' ')
for i in range(0,tam,2):
    print(a[i],end=' ')

# Exibindo os elementos dos índices ímpares
print('\nElementos nos índices ímpares:', end=' ')
for i in range(1,tam,2):
    print(a[i],end=' ')
