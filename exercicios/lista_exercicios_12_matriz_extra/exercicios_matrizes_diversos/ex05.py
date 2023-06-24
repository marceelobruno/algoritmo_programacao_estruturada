"""
http://www.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

2. Faça um algoritmo que construa uma matriz 50 por 50 de números reais e
depois de construída, colocar o conteúdo de sua diagonal principal dentro
de um vetor e depois do vetor montado, imprimir o vetor.

OBS: Acrescentei vetor diagonal secundária
"""
from random import randint

# Ordem da matriz
tam = 50

# Criando a matriz
mat = [[None] * tam for i in range(tam)]

# Criando os vetores
vet_prin = [None] * tam
vet_sec = [None] * tam

# Preenchendo a matriz e o vetor
for i in range(tam):
    for j in range(tam):
        mat[i][j] = randint(0,30)
        if i == j:
            vet_prin[i] = mat[i][j]
        elif i + j == tam -1:
            vet_sec[i] = mat[i][j]

# Printando a matriz
print('Matriz:')
for i in range(tam):
    for j in range(tam):
        print(f'{mat[i][j]:4}',end=' ')
    print()

# Printando os vetores
print('\nVetor Diagonal Principal:',vet_prin)
print('Vetor Diagonal Secundária:',vet_sec)
