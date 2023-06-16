"""
2. Faça um programa que leia 10 números e os apresente na ordem inversa.
"""
import random

n = 10
v = []

print(f'Informe os {n} elementos do vetor V:')
while len(v) < 10:
    num = random.randint(1,10)
    v.append(num)

print('V =', v)
v.reverse()
print('Vetor V na ordem inversa:', v)
