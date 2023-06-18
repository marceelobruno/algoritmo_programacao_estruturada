"""
6. Faça um programa que receba do usuário um vetor com 10 posições.
Em seguida exiba o maior e o menor elemento do vetor.
"""
pos = 5
y = [None] * pos
menor = y[0]
maior = y[0]

for i in range(pos):
    print(f'Digite o {i+1}° valor do vetor:', end=' ')
    y[i] = int(input())

for e in range(pos):
    if y[e] > maior:
        maior = y[e]
    elif y[e] < menor:
        menor = y[e]

print('Menor valor do vetor ', menor)
print('Maior valor do vetor ', maior)
