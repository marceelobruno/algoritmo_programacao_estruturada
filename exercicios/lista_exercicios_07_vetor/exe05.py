"""
5. Escreva um programa que receba um vetor V de N números inteiros (N será lido),
determine e exiba o maior e o menor elemento deste vetor e seus respectivos
índices. OBS: suponha a inexistência de valores repetidos.
"""
from random import randint
# n = int(input('Digite o tamanho do vetor A: '))
n = 6
a = [None]*n

print('Informe os elementos do vetor A: ')
for i in range(n):
    a[i] = randint(1,30)

print('A: ',a)

maior = max(a)
menor = min(a)

print(f'Maior elemento {maior}, está no índice {a.index(maior)}')
print(f'Menor elemento {menor}, está no índice {a.index(menor)}')
