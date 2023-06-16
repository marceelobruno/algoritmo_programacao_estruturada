"""
Escreva um programa que leia um vetor de 10 elementos. 
O programa deve informar a quantidade de números ímpares existentes no vetor.
OBS: Os valores armazenados no vetor serão informados pelo usuário, ou gerados pelo computador.
"""
import random
n = 4
cont = 0
v = [None] * n

print('Informe os elementos do vetor:')
for i in range(n):
    v[i] = random.randint(0,9)

print('Vetor V =',v)

for j in range(n):
    if v[j] % 2 == 1:
        cont += 1

if cont > 0:
    print(f'Há {cont} elemento(s) ímpar(es) no vetor.')
else:
    print('Não há elementos ímpares no vetor.')
