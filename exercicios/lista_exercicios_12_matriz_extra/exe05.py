"""
5. Leia uma matriz 5 x 5. Leia também um valor X.
O programa deverá fazer uma busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna) ou uma mensagem de “não encontrado”.
"""
import random

ordem = 5
mat = [[None]*ordem for i in range(ordem)]
x = int(input('Informe um número: '))
aux = False
lin = 0
col = 0

print('Matriz:')
for i in range(ordem):
    for j in range(ordem):
        mat[i][j] = random.randint(1,50)
        if mat[i][j] == x:
            aux = True
            lin = i
            col = j
        print(f'{mat[i][j]:4}',end='')
    print()

if aux:
    print(f'\n{x} está localizado na linha {lin} e coluna {col}.')
else:
    print(f'\n{x} não encontrado na matriz')
