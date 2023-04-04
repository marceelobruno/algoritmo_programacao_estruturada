"""Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles."""

valor_1 = int(input("Digite um número inteiro: "))
valor_2 = int(input("Digite outro número inteiro: "))
valor_3 = int(input("Digite mais um número inteiro: "))

# Using if ... elif ... else structure
if valor_1 > valor_2 and valor_1 > valor_3:
    print(f'Este é o maior número informado {valor_1}')

elif valor_2 > valor_1 and valor_2 > valor_3:
    print(f'Este é o maior número informado {valor_2}')

else:
    print(f'Este é o maior número informado {valor_3}')
