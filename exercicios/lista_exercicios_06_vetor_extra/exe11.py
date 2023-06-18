"""
14. Faça um programa que leia um vetor de 10 posições e verifique se
existem valores iguais e os escreva na tela.
"""
import random

n = 6
a = [None] * n
rep_a = []

print(f"Preencha {n} elementos para o vetor:")
for i in range(n):
    a[i] = random.randint(1, 6)

for e in range(n):
    if a.count(a[e]) > 1:
        if a[e] in rep_a:
            continue
        rep_a.append(a[e])

print('Vetor =', a)
print(f'Valores repetidos do vetor: {rep_a}')
