"""
1. Escreva uma função chamada menor que receba 3 números e retorne o menor
deles. Faça também um programa para testar a função.
"""

def menor(valor1: int, valor2: int, valor3: int) -> int:
    if valor1 < valor2 and valor1 < valor3:
        return valor1
    elif valor2 < valor1 and valor2 < valor3:
        return valor2
    else:
        return valor3

#  Programa Principal

print('Informe 3 valores: ')
v1 = int(input())
v2 = int(input())
v3 = int(input())

resultado = menor(v1,v2,v3)
print(f'Menor valor: {resultado}')