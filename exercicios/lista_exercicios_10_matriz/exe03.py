"""
3. Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem
será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B
corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se
o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0.
"""
n = int(input('Ordem da matriz: '))
a = [[None] * n for i in range(n)]
b = [[None] * n for i in range(n)]

print('\nDigite os elementos da matriz: ')
for i in range(n):
    print(f'Informe os elementos da {i+1}ª linha:')
    for j in range(n):
        a[i][j] = int(input())


print('\nMatriz A:')
for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:4}', end=' ')
    print()

print('\nMatriz B:')
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:  # i+j == n-1 (representa matriz secundária)
            b[i][j] = 0
        else:
            b[i][j] = a[i][j] + (i + j)
        print(f'{b[i][j]:4}', end=' ')
    print()
