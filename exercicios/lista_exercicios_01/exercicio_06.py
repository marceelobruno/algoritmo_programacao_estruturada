"""
6 - Faça um programa que efetue a apresentação do valor da conversão em real (R$)
de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação
do dólar e também a quantidade de dólares disponíveis com o usuário.
"""

dolar_dia = float(input('Digite o valor, em reais da cotação do dólar do dia R$: '))

montante_dinheiro = float(input('Quantos dólares você possui US$: '))

print(f'Você possui R$ {montante_dinheiro * dolar_dia:.2f}')
