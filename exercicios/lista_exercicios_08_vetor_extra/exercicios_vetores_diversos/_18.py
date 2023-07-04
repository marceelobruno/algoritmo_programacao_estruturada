"""
65. Faça um programa em C que leia um array de 20 inteiros e imprima
o menor e o maior valor dentre os elementos do array e suas posições.
"""
import random

tam = 10
vet = [None]*tam

for i in range(tam):
    vet[i] = random.randint(1,50)

menor = vet[0]
maior = vet[0]

for i in range(tam):
    if vet[i] < menor:
        menor = vet[i]
    elif vet[i] > maior:
        maior = vet[i]

print(f'''
      Vetor original: {vet}
      Menor elemento: {menor}, Posição {vet.index(menor)}.
      Maior elemento: {maior}, Posição {vet.index(maior)}.''')
