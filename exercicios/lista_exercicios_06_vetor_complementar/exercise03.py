"""
3. Escreva um programa para ler 6 números. Após a leitura dos números,
verifique, para cada um deles, se é distinto, ou seja, não possui repetição.
"""
import random

n = 6
v = [None] * n

for i in range(n):
    v[i] = random.randint(1, 10)
print('V =', v)

for e in v:
    if v.count(e) > 1:
        print(e,' repete')
    else:
        print(e,' não repete')
