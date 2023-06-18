"""
1. Escreva um programa que leia um vetor contendo N elementos inteiros (N será
lido), calcule e exiba:
• A quantidade de elementos pares;
• A quantidade de elementos ímpares;
• A soma de todos os elementos;
• A média dos elementos do vetor.
"""

n = int(input('Digite o tamanho do vetor: '))
v = [None] * n

print('Informe os elementos do vetor V: ')
for i in range(n):
    v[i] = int(input())
print('V = ', v)

contPares = 0
contImpares = 0

for i in range(n):
    if v[i] % 2 == 0:
        contPares += 1
    else:
        contImpares += 1

soma = sum(v)

print(f'Quantidade de elementos: {contPares} pares e {contImpares} ímpares. \
    Soma dos elementos: {soma} e Média {soma/n:.2f}.')
