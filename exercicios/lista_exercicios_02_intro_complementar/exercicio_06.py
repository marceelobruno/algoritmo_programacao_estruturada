"""
6 - As Ilhas Weblands formam um reino independente nos mares do Pacífico.
Como é um reino recente, a sociedade é muito influenciada pela informática.
A moeda oficial é o Bit e existem notas de B$ 50, B$ 10, B$ 5 e B$ 1.

Você foi contratado(a) para ajudar na programação dos caixas automáticos de um
grande banco das Ilhas Weblands. Os caixas eletrônicos das Ilhas Weblands operam
com todos os tipos de notas disponíveis, mantendo um estoque para cada valor de cédula.

Os clientes do banco utilizam os caixas eletrônicos para efetuar retiradas de um certo
número inteiro de Bits. Sua tarefa é escrever um programa que, dado o valor de Bits
desejado pelo cliente, determine o número de cada uma das notas necessário para totalizar
esse valor, de modo a minimizar a quantidade de cédulas entregues.

Exemplo:
Para B$ 72 seriam as seguintes notas:
- 1 nota de B$ 50
- 2 notas de B$ 10
- 0 notas de B$ 5
- 2 notas de B$ 1
"""

bits_desejados = int(input('Informe a quantidade de bits desejados para o saque: B$'))

cinquenta = bits_desejados // 50
resto = bits_desejados % 50
dez = resto // 10
resto_2 = resto % 10
cinco = resto_2 // 5
um = resto_2 % 5

print(f'Para B${bits_desejados} seriam as seguintes notas: \
    \n- {cinquenta} nota(s) de B$50 \
    \n- {dez} nota(s) de B$10 \
    \n- {cinco} nota(s) de B$5 \
    \n- {um} nota(s) de B$1')
