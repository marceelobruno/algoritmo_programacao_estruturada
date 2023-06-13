"""
Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio.
Faça um programa que leia um número e determine se ele é ou não primo.
"""

numero = int(input('Digite um valor para saber se o número é primo: '))

if numero <= 1:
    eh_primo = False
else:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break
if eh_primo:
    print(f'{numero} é primo!')
else:
    print(f'{numero} não é primo!')
