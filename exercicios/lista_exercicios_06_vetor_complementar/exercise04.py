"""
4. Escreva um programa para ler 6 números distintos, ou seja, não podem repetir.
Exiba os números lidos.
"""
tam = 6
numeros = []

print(f'Informe {tam} números distintos:')
while len(numeros) < 6:
    num = int(input())
    if num in numeros:
        print('Número existente! Informe outro número:')
    else:
        numeros.append(num)

print('Números lidos: ', *numeros)
