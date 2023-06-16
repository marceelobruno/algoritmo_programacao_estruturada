"""
1. Faça um programa que leia 5 valores inteiros, armazeno-os em um vetor,
calcule e apresente a soma destes valores.
"""
from random import randint

tam = 5
a = [None]*tam

print('Digite os elementos do vetor A:')
for i in range(tam):
    a[i] = randint(1,5)

print('A =',a)
print(f'\nA soma dos elementos do vetor A é: {sum(a)}')

"""
Altere o programa acima para calcular e apresentar a média dos valores do vetor
e exibir aqueles que são maiores e menores que a média.
"""
media = sum(a)/tam
maior = []
menor = []

for e in a:
    if e > media:
        maior.append(e)
    else:
        menor.append(e)

print(f'A média dos elementos do vetor A é: {media}')
print(f'Elementos do vetor A acima da média: {maior}')
print(f'Elementos do vetor A abaixo da média: {menor}')
