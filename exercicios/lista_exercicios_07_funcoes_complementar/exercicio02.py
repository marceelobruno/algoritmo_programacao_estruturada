"""
2. Escreva uma função chamada primo para determinar se um número é primo ou não.
A função deve receber um número inteiro, retornar True se o número for primo, ou False
caso contrário.
Escreva também um programa que, usando a função primo criada, exiba os números primos entre 1 e 100.
"""


def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True


# Programa Principal - Primos de 1 a 100
for e in range(1, 101):
    if eh_primo(e):
        print(e, ' ', end='')
