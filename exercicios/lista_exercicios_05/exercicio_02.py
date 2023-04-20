"""
2 - Faça um programa que leia um número N, inteiro, e some todos os números
de 1 até N, mostrando o resultado.
"""

limite = int(input('Digite o valor de N: '))

soma = 0

for i in range(1, limite+1):
    soma += i

print(f'A soma do valores entre 1 e {limite} é {soma}.')
