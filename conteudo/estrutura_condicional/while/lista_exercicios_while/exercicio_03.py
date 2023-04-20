"""
3 - Faça um programa que leia vários números, determine e mostre o maior e o
menor deles. OBS: a leitura do número 0 (zero) encerra o programa.
"""

valor = int(input('Informe um valor: '))

menor = maior = valor

while valor != 0:
    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

    valor = int(input('Informe um outro valor: '))

print(f'Maior {maior}')
print(f'Menor {menor}')
