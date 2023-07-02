"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

04. Faça um programa para ler N valores inteiros e armazená-los em um vetor.
O programa deve contar quantos valores pares ele possui e somar os valores ímpares.
"""
import random

n = int(input('Tamanho: '))

vetor = [None]*n
cont_par = 0
soma_impar = 0

print('Informe os elementos:')
for i in range(n):
    vetor[i] = int(input())
    if vetor[i] %2==1:
        soma_impar += vetor[i]
    else:
        cont_par += 1

print(f'''
Vetor: {vetor}
Quantidade de pares: {cont_par}
Soma dos ímpares: {soma_impar}
      ''')
