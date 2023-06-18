"""
31. Faça um programa que leia dois vetores de 10 elementos.
Crie um vetor que seja a união entre os 2 vetores anteriores, ou seja,
que contêm os números dos dois vetores. OBS: Não deve conter números repetidos.
"""
import random

tam = 5
a = [None] * tam
b = [None] * tam
c = []

print(f'Preencha os vetores A e B com {tam} elementos')
for i in range(tam):
    print(f'\nInforme o {i+1}° elemento de A: ')
    a[i] = random.randint(1, 10)
    print(f'Informe o {i+1}° elemento de B: ')
    b[i] = random.randint(1, 10)

rep_c = a + b

for j in range(len(rep_c)):
    if rep_c.count(rep_c[j]) > 0:
        if rep_c[j] in c:
            continue
        c.append(rep_c[j])

c.sort()

print(f'''
    Vetor A = {a}
    Vetor B = {b}
    União entre os vetores A e B = {c}''')
