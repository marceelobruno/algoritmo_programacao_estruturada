"""
Escreva um programa que leia um vetor contendo 30 elementos inteiros e exiba:
a) A média os elementos positivos do vetor;
b) A média dos elementos negativos do vetor.
"""
import random

tam = 10
v = [None]*tam
soma_pos = 0
cont_pos = 0
soma_neg = 0
cont_neg = 0

for i in range(tam):
    print(f'Informe o {i+1}° Elemento:')
    v[i] = random.randint(-10,10)
    if v[i] > 0:
        soma_pos += v[i]
        cont_pos += 1
    else:
        soma_neg += v[i]
        cont_neg +=1

print('vetor =',v)

print(f'''\n
Média dos elementos positivos do vetor: {soma_pos/cont_pos:.2f}
Média dos elementos negativos do vetor: {soma_neg/cont_neg:.2f}''')
