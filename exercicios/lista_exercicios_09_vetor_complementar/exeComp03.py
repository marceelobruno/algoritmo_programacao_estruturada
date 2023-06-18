"""
4. Faça um programa que leia 5 números inteiros, armazene-os em um vetor,
solicite um valor de referência inteiro e:
a) Imprima os números do vetor que são maiores que o valor referência
b) Retorne quantos números armazenados no vetor são menores que o valor de referência
c) Retorne quantas vezes o valor de referência aparece no vetor
"""
import random
n = 5
cont = 0
menor = 0
maior = []
a = []

print(f'Informe {n} elementos para o vetor:')
while len(a) < 5:
    num = random.randint(1,8)
    a.append(num)
print('Vetor A =', a)

ref = int(input('Agora informe um valor para referência: '))

for i in a:
    if i > ref:
        maior.append(i)
    else:
        menor += 1
    if i == ref:
        cont += 1

print(f'Valores maiores que {ref}: {maior}.')
print(f'Existem {menor} elementos menores que {ref} e o valor {ref} aparece {cont} vezes no vetor.')
