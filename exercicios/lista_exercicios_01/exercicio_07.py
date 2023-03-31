"""
7 - O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição.
Faça um programa que leia o peso do prato montado pelo cliente (em quilos) e
exiba o valor a pagar. Assuma que a balança já desconte o peso do prato.
"""

VALOR_KG = 25.00

peso_prato = float(input('Digite o peso do prato: '))

valor_prato = peso_prato * VALOR_KG

print(f'O valor do prato informado é de R$ {valor_prato:.2f}')
