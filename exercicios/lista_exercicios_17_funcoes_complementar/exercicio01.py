"""
1. Escreva uma função chamada vogal que receba uma letra e verifique se a letra é uma
vogal, retornando o valor True nesse caso, ou o valor False caso contrário.
Escreva também um programa que leia uma frase e, usando a função vogal criada,
imprima a quantidade de vogais existentes na frase lida.
"""


def vogal(letra):
    if letra in 'aeiouAEIOU':
        return True
    return False


def total_vogais(frase):
    cont = 0
    for caractere in frase:
        if vogal(caractere):
            cont += 1
    return cont


frase = input('Informe uma frase: ')

print(f'A frase possui {total_vogais(frase)} vogais.')
