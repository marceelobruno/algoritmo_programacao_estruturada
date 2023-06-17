"""
2. Crie um programa que receba 6 valores inteiros e, em seguida,
mostre na tela os valores lidos.
"""
tam = 6
a = []

print(f'Informe {tam} números')

for i in range(tam):
    print(f'Digite o {i + 1}° valor: ', end='')
    num = int(input())
    a.append(num)

print(f'\nValores atribuídos ao vetor A: {a}')
