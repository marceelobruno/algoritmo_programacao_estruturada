"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

02. Faça um programa que lê 8 números inteiros e os armazena em um vetor,
e calcula e mostra dois vetores resultantes:
• O primeiro vetor resultante deve conter os números positivos;
• O segundo deve conter os números negativos.
Cada vetor resultante vai ter, no máximo, oito posições, que poderão não
ser completamente utilizadas. Guarde em variáveis a quantidade de valores
armazenados em cada vetor resultante.
"""
import random

tam = 8
vet = []
vet_pos = []
vet_neg = []

# preenchendo os vetores:
print(f'Digite {tam} números inteiros:')
for i in range(tam):
    vet.append(random.randint(-10, 10))
    if vet[i] >= 0:
        vet_pos.append(vet[i])
    else:
        vet_neg.append(vet[i])

# exibindo vetores
print(f'''
Vetor Inicial: {vet}\nVetor Positivos: {vet_pos}\nVetor Negativos: {vet_neg}''')
