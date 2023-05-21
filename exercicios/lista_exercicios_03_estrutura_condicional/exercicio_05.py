"""
A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de
5% sobre o total de vendas daquele vendedor, mas essa comissão nunca deve ser
inferior ao salário-mínimo.

Escreva um programa que leia o valor total das vendas de um vendedor e escreva
seu salário.
"""

SALARIO = 1320.00
COMISSAO = 0.05

vendas_total = float(input('Vendedor(a), qual foi o valor total de vendas este mês: R$ '))

bonus = vendas_total * COMISSAO

if bonus > SALARIO:
    print(f'Vendedor(a), seu salário será R${bonus:.2f}.')
else:
    print('Comissão abaixo do salário mínimo!')
