"""Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles."""

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite outro número inteiro: "))
num_3 = int(input("Digite mais um número inteiro: "))

# Using if ... elif ... else structure
if num_1 > num_2 and num_1 > num_3:
    print(f'Este é o maior número informado {num_1}')

elif num_2 > num_1 and num_2 > num_3:
    print(f'Este é o maior número informado {num_2}')

else:
    print(f'Este é o maior número informado {num_3}')
