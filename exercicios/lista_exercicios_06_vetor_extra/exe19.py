"""
29. Faça um programa que receba 6 números inteiros e mostre:
• Os números pares digitados;
• A soma dos números pares digitados;
• Os números ímpares digitados;
• A quantidade de números ímpares digitados;
"""
from random import randint

tam = 6
v = [None] * tam
par = []
impar = []
somaPar = 0
qtdImpar = 0

print(f'Preencha o vetor com {tam} números inteiros:')
for i in range(tam):
    v[i] = randint(1, 6)
    if v[i] % 2 == 0:
        par.append(v[i])
        somaPar += v[i]
    else:
        impar.append(v[i])
        qtdImpar += 1

print(f'''
      Vetor V = {v}
      Números pares do vetor: {par} e a soma entre eles: {somaPar}.
      Números ímpares do vetor: {impar} e a quantidade deles: {qtdImpar}.
      ''')
