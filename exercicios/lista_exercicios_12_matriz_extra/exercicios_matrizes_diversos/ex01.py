"""
https://www.galirows.com.br/meublog/programacao/exercicios-simples-com-matrizes/

Algoritmo 1 - Elabore um algoritmo que preencha duas matrizes 10x10 com 
valores aleatórios 0 e 1 e em seguida, determine se as matrizes são iguais
(possuem os mesmos valores em cada posição).
"""
import random

tam = 10

mat_a = [[None] * tam for i in range(tam)]
mat_b = [[None] * tam for i in range(tam)]
cont_dif = 0

# Preenchendo as matrizes A e B
for i in range(tam):
    for j in range(tam):
        mat_a[i][j] = random.randint(0, 1)
        mat_b[i][j] = random.randint(0, 1)

        # Verificando se as matrizes são diferentes
        if mat_a[i][j] != mat_b[i][j]:
            cont_dif += 1

# Imprimindo as matrizes
print('Matriz A')
for i in range(tam):
    for j in range(tam):
        print(f'{mat_a[i][j]:4}', end=' ')
    print()

print('\nMatriz B')
for i in range(tam):
    for j in range(tam):
        print(f'{mat_b[i][j]:4}', end=' ')
    print()

if cont_dif > 1:
    print('\nMatrizes diferentes.')
else:
    print('\nMatrizes iguais.')
