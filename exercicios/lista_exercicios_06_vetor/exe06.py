"""
6. Escreva um programa que leia um vetor de N números inteiros (N será lido),
inverta a ordem dos elementos do vetor e exiba o vetor invertido.
Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
OBS: É necessário inverter os elementos do vetor, não basta imprimi-los em
ordem inversa!
"""
from random import randint
# n = int(input('Digite o tamanho do vetor V: '))
n = 5
v = [None]*n

print('Informe os elementos do vetor V: ')
for i in range(n):
    v[i] = randint(1,51)
print('V = ',v)

# Invertendo os elementos do vetor
v.reverse()
print('V = ',v)
