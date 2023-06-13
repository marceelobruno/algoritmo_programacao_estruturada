"""
Escreva um programa que preencha uma matriz quadrada de ordem 3 com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente),
calcule e exiba:
• A soma dos elementos de cada linha;
• A soma dos elementos de cada coluna;
• A soma dos elementos da diagonal principal da matriz;
• A soma dos elementos da diagonal secundária da matriz;
• A soma de todos os elementos da matriz.

[1,2,3],
[7,8,9],
[4,5,6]
"""
import random

matriz_1 = [[None] * 3 for i in range(3)]

matriz_2 = [[random.randint(1, 9) for j in range(3)] for i in range(3)]

# contador = 0
somador_linhas = 0
somador_colunas = 0
somador_diag_principal = 0
somador_diag_sec = 0

for i in range(len(matriz_2)):
    # for j in range(len(matriz_2[i])):
    for j in range(len(matriz_2)):
        somador_linhas += matriz_2[i][j]
        # somador_colunas += matriz_2[i]
        # if i == j:
        #     somador_diag_principal += matriz_2[i][j]
        # if (i + j) == len(matriz_2) - 1:
        #     somador_diag_sec += matriz_2[i][j]
        print(f'{matriz_2[i][j]}', end=" ")
    print()

print(somador_linhas)
print(somador_diag_principal)
print(somador_diag_sec)

# 123, i = 0 j = 2 i+j= len(matriz_2) - 1
# 123, i = 1 j = 1 i+j=2
# 123, i = 2 j = 0 i+j=2
