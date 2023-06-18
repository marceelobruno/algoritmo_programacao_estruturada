"""
22. Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares os valores do primeiro e nas posições ímpares os valores do segundo.
"""
import random

tam = 10
a = [None]*tam
b = [None]*tam
c = []

print(f'Informe {tam} valores para os vetores A e B respectivamente:')
for i in range(tam):
    print(f'Digite o {i+1}° valor de A:')
    a[i] = random.randint(1,10)
    print(f'Digite o {i+1}° valor de B:')
    b[i] = random.randint(11,20)
    c.append(a[i])
    c.append(b[i])

print('\nVetor A =',a)
print('Vetor B =',b)
print('Vetor C =',c)
