"""
1. Escreva um programa que leia um vetor A de N números inteiros (N será lido) e
um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os
respectivos elementos de a multiplicados por K.
Ex: A = [1,2,3], K = 5, B = [5,10,15].
"""

# Leitura do tamanho do vetor
tam = int(input('Informe o tamanho do vetor "A": '))

# Inicializando os vetores
a = [None] * tam
b = [None] * tam

# Leitura do vetor A
print('Digite os elementos do vetor A:')
for i in range(tam):
    a[i] = int(input(f'A[{i}]:'))

# Atribuindo um valor para K
k = int(input('Informe um valor para "K": '))

# Geração do vetor B
for i in range(tam):
    b[i] = a[i] * k

# Exibindo os resultados
print()
print('A = ', a)
print('K = ', k)
print('B = ', b)
