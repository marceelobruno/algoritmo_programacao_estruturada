"""
1 - A Companhia de Carros Usados João Honesto paga seus empregados um salário de
R$ 1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais
5% do valor da venda.

Escreva um programa que leia o nome, o número de carros vendidos e o valor
total das vendas de um vendedor, e calcule e exiba o seu salário.
"""

SALARIO = 1000
COMISSAO = 200
PORCENTAGEM_VENDA_TOTAL = 0.05

vendedor = input('Informe o nome do vendedor: ')

carros_vendidos = int(input('Quantos carros foram vendidos: '))

valor_vendas_total = float(input('Valor total das vendas feito pelo vendedor R$: '))

salario_final = (carros_vendidos * COMISSAO) + (PORCENTAGEM_VENDA_TOTAL * valor_vendas_total) + SALARIO

print(f'O salário do vendedor {vendedor} esse mês será de R$ {salario_final:.2f}')
