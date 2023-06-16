"""
Faça um programa que receba 10 números inteiros, armazene em um vetor e
exiba a soma dos números ímpares e a soma dos números pares.
"""
import random

tam = 10
a = [0] * tam
par = 0
impar = 0

print('Informe os valores do vetor: ')
for i in range(tam):
    a[i] = random.randint(1, 20)
    if a[i] % 2 == 0:
        par += a[i]
    else:
        impar += a[i]

print('Vetor A =', a)
print(f'Soma dos números pares: {par}.')
print(f'Soma dos números ímpares: {impar}.')
