"""
11. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre
a quantidade de números negativos e a soma dos números positivos desse vetor.
"""
tam = 10
v = [None] * tam
cont = 0
pos = 0

print(f'Preencha o vetor com {tam} números reais:')
for i in range(tam):
    num = float(input())
    if num > 0:
        pos += num
    else:
        cont += 1

print('Soma dos elementos positivos:', pos)

if cont > 0:
    print('Quantidade de elementos negativos no vetor: ', cont)
else:
    print('Não há elementos negativos no vetor.')
