"""
2. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida.
"""
n = 5
mat = [[None]*n for i in range(n)]

print('Matriz:')
for i in range(n):
    for j in range(n):
        if i == j:
            mat[i][j] = 1
        else:
            mat[i][j] = 0
        print(f'{mat[i][j]:4}',end=' ')
    print()
