"""
4. Faça um programa que leia duas matrizes de inteiros e gere uma
terceira matriz que corresponderá a soma das duas matrizes lidas.
A ordem das matrizes também será lida.
O programa deverá conter as seguintes funções:
• Uma função para gerar e ler uma matriz, sendo passados como
parâmetros a ordem da matriz.
• Uma função para exibir uma matriz em sua representação clássica (linhas e colunas).
• Uma função para somar duas matrizes.
"""


# Função para gerar e ler uma matriz
def gera_matriz(num):
    mat = [[None] * num for i in range(num)]

    for i in range(num):
        for j in range(num):
            mat[i][j] = int(input())
    return mat


# Função para somar duas matrizes
def soma_matriz(mat1, mat2):
    n = len(mat1)
    mat_3 = [[None] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            mat_3[i][j] = mat1[i][j] + mat2[i][j]
    return mat_3


# Função para imprimir uma matriz
def exibe_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(f'{matriz[i][j]:4}', end=' ')
        print()


tam = 3
# Gerando Matrizes A e B
print('Digite os elementos da Matriz A:')
mat_a = gera_matriz(tam)
print('\nDigite os elementos da Matriz B:')
mat_b = gera_matriz(tam)

# Imprimindo Matrizes A e B
print('\nMatriz A:')
exibe_matriz(mat_a)
print('\nMatriz B:')
exibe_matriz(mat_b)

# Gerando Matriz C
mat_c = soma_matriz(mat_a, mat_b)
# Imprimindo Matriz C
print('\nMatriz C:')
exibe_matriz(mat_c)
