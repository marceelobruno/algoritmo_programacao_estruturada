"""
Escreva um programa que receba do usuário um vetor com 6 valores inteiros e apresente
o maior e o menor elemento e suas respectivas posições em que os mesmos foram encontrados.
OBS: Caso existam números iguais mostre a posição da primeira ocorrência.
"""
N = 6
a = []

print(f'Informe os {N} elementos do vetor A:')
while len(a) < N:
    elemento = int(input())
    a.append(elemento)
print('Vetor A =', a)

menor = min(a)
indMenor = a.index(menor)
maior = max(a)
indMaior = a.index(maior)

print(f'Menor elemento do vetor: {menor}, posição {indMenor}.')
print(f'Maior elemento do vetor: {maior}, posição {indMaior}.')

for i in a:
    if a.count(i) > 1:
        posicao = a.index(i)
        print(f'Números do vetor que se repetem: {i}, posição: {posicao}')

# Usando For
print('\nUsando for para descobrir o maior/menor elemento e suas posições:')
forMenor = a[0]
posMenor = 0
for e in range(N):
    if a[e] < forMenor:
        forMenor = a[e]
        posMenor = e
print(f'Menor elemento do vetor: {forMenor}, posição {posMenor}.')

forMaior = a[0]
posMaior = 0
for j in range(N):
    if a[j] > forMaior:
        forMaior = a[j]
        posMaior = j
print(f'Maior elemento do vetor: {forMaior}, posição {posMaior}.')
