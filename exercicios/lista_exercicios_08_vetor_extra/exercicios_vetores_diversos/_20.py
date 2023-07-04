"""
73. Escreva um programa em C que leia um array de 20 inteiros, calcule e imprima:
a. A moda dos elementos no array (elemento mais freqüente).
b. A mediana dos elementos no array (elemento central)
c. A média
"""
from random import randint

tamanho = int(input('Digite o tamanho do vetor: '))
vetor = []

# preenchendo o vetor
for i in range(tamanho):
    vetor.append(randint(1, 8))

# criando as variáveis
moda = []
mediana = 0
media = 0

# calculando a moda
frequency = {}
for i in vetor:
    frequency.setdefault(i, 0)
    frequency[i] += 1
frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        moda.append(i)

# calculando a média
media = round(sum(vetor) / len(vetor),3)

# ordenando o vetor
vetor.sort()

# calculado a mediana se a quantidade de elementos do vetor for par
if len(vetor) % 2 == 0:
    mediana_1 = vetor[(len(vetor) // 2)]
    mediana_2 = vetor[(len(vetor) // 2) - 1]
    mediana = (mediana_1 + mediana_2) / 2

# calculando a mediana se a quantidade de elementos do vetor for ímpar
else:
    mediana = vetor[(len(vetor) // 2) + 1]

print(f'''
Vetor: {vetor}
Moda: {(moda)}
Mediana {mediana}
Média {media}''')
