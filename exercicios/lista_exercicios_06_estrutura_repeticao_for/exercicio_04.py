"""
4 - Faça um programa que leia 20 números inteiros, determine e mostre o maior
deles.
"""

maior = -65000

for i in range(5):
    valor = int(input(f'Digite o {i}° valor: '))
    if valor > maior:
        maior = valor

print(f'Este é o maior número informado: {maior}')
