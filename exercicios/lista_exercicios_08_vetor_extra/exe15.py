"""
20. Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene
em um vetor com 10 posições. Preencha um segundo vetor apenas com os números ímpares
do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
"""
import random
n = 10
v1 = [None]*n
v2 = []

print(f'Atribua {n} valores para o vetor:')
for i in range(n):
    v1[i] = random.randint(0,50)
    if v1[i] % 2 == 1:
        v2.append(v1[i])

print('Vetor 1 =', v1)
print('Vetor 2 =', v2)
