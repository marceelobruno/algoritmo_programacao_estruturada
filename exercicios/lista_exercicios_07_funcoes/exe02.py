"""
2. Escreva uma função chamada fatorial que receba um número inteiro e retorne
seu fatorial. Faça também um programa para testar a função.
"""

def fatorial(numero: int) -> int:
    fat = 1
    for i in range(2, numero+1):
        fat*=i
    return fat

num = int(input('Digite um número inteiro: '))
print(f'{num}! = {fatorial(num)}')
