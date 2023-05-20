SALARIO = 1000.00
COMISSAO = 200.00
VALOR_VENDA = 0.05

nome = input('Digite o nome do vendedor(a): ').title()

carros_vendidos = int(input('Quantos carros foram vendidos: '))

valor_total = float(input('Valor total da venda: R$ '))

salario_final = (COMISSAO * carros_vendidos) + (VALOR_VENDA * valor_total) + SALARIO

print(f'{nome}, o seu salário final é R$ {salario_final:.2f}')
