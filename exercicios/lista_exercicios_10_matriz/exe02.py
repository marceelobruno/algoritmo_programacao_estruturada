"""
2. Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.
"""
n = int(input('Informe o valor da matriz quadrada: '))

a = [[None] * n for i in range(n)]
b = []

print('\nAtribuindo os valores para matriz A')
for i in range(n):
    print(f'Valores para a {i+1}ª linha:')
    for j in range(n):
        a[i][j] = int(input())

# Imprimindo matriz A
print('\nMatriz A:')
for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:4}', end=' ')
    print()

# Capturando os valores da diagonal principal da matriz A
# print('\nDiagonal principal:')
for i in range(n):
    for j in range(n):
        if a[i] == a[j]: # if i == j:
            b.append(a[i][j]) # print(f'{a[i][j]:4}',end=' ')

# Imprimindo diagonal principal
print('\nDiagonal Principal: ', b)
