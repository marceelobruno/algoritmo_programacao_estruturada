"""
1 - Faça um programa que leia 30 números inteiros,
calcule e mostre a soma deles. OBS: não use o comando for, use while.
"""
TOTAL = 5
quantidade = 0
soma = 0

valor = int(input('Digite um valor: '))
while quantidade < TOTAL:
    soma += valor
    quantidade += 1
    valor = int(input('Digite um outro valor: '))

print(f'A Soma de todos os números digitados foi {soma}')
