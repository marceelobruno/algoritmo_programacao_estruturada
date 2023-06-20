"""
1. Faça um programa que leia uma frase e determine
a quantidade de brancos contidos na mesma.
"""
frase = input('Frase: ')
cont = 0

for i in frase:
    if i == ' ':
        cont +=1

print('Quantidade de brancos na frase: ',cont)
