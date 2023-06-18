"""
3. Escreva um programa que leia N números inteiros (máximo 20) e armazene em um
vetor X. Calcule a média dos elementos do vetor e informe quantos elementos
estão abaixo da média do conjunto.

Crie as seguintes funções:
• Uma função que faça a leitura dos elementos de um vetor de inteiros.
Essa função deve receber como parâmetro o número de elementos do vetor e deve
retornar o vetor preenchido;
• Uma função que calcule a média dos elementos de um vetor. Essa função deve
receber como parâmetro um vetor e retornar a média dos elementos dele;
• Uma função que receba um vetor e um número, e retorne quantos elementos do
vetor estão abaixo desse número.
"""

n = int(input('Digite o tamanho de N: '))

x = []

print(f'Informe {n} elementos para o vetor X: ')
while len(x) < n:
    num = int(input())
    x.append(num)

print('X =', *x)
