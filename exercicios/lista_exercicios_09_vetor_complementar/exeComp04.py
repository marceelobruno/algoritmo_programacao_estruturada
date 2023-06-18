"""
4. Faça um programa que leia N números inteiros, armazene em um vetor A
e mostre o maior e o menor deles.
"""
n = int(input('Digite a quantidade de números: '))
a = [None] * n

numero = int(input('Entre com o 1º número inteiro: '))
a[0] = numero
maior = numero
menor = numero

for i in range(1, n):
    print(f'Entre com o {i+1}º número inteiro: ', end='')
    a[i] = int(input())

    if a[i] > maior:
        maior = a[i]
    else:
        if a[i] < menor:
            menor = a[i]

print('\nO menor número do vetor:', menor)
print('O maior número do vetor:', maior)
