"""
http://www.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

1. Faça um programa que lê 10 números inteiros do teclado e armazene em um vetor.
Ao final imprima o vetor armazenado nos dois sentidos.
"""
import random

tam = 10
vet = [None]*tam

# preenchendo o vetor com valores aleatórios
for i in range(tam):
    vet[i] = random.randint(0,10)

# imprimindo o vetor na ordem em que foi preenchido
print('Vetor na ordem original: ',vet)

# invertendo a ordem do vetor usando função
vet.reverse()

# imprimindo o vetor na ordem reversa
print('Vetor na ordem reversa: ',vet)
