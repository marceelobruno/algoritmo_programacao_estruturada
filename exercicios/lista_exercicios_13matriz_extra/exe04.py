"""
4. Leia uma matriz 4 x 4, imprima a matriz e retorne
a localização (linha e a coluna) do maior valor.
"""
from random import randint

o = 4
m = [[None]*o for i in range(o)]
lin = 0
col = 0
maior = [0][0]

print('Matriz:')
for i in range(o):
    for j in range(o):
        m[i][j] = randint(1,30)
        if m[i][j] > maior:
            maior = m[i][j]
            lin = i
            col = j
        print(f'{m[i][j]:4}', end='')
    print()

print(f'''
Localização do maior elemento da matriz:
Linha: {lin} | Coluna: {col}''')
