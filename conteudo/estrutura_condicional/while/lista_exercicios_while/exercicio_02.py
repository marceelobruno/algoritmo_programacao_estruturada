"""
2 - Faça um programa que leia vários números, calcule e exiba a média desses
números.
OBS: a leitura do número 999 indica o fim dos dados de entrada e não deve ser
computado na média
"""

FLAG = 999
contador = 0
soma = 0

valor = int(input('Digite um valor: '))

while valor != FLAG:
    soma += valor
    contador += 1
    valor = int(input('Digite outro valor: '))

print(f'A média dos números informados é: {soma // contador}')
