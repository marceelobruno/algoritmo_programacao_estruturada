"""
30. Faça um programa que leia dois vetores de 10 elementos.
Crie um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja,
que contêm apenas os números que estão em ambos os vetores.
OBS: Não deve conter números repetidos.
"""
from random import randint

tam = 5
a = [None]*tam
b = [None]*tam
c = []

print(f'Preencha os vetores A e B com {tam} elementos')
for i in range(tam):
    print(f'\nDigite o {i+1}° valor para A:')
    a[i] = randint(1,10)
    print(f'Digite o {i+1}° valor para B:')
    b[i] = randint(1,10)

for j in range(tam):
    if a[j] in b:
        if a[j] in c:
            continue
        c.append(a[j])

print(f'''
    Vetor A = {a}
    Vetor B = {b}
    Intersecção entre os vetores A e B = {c}''')
