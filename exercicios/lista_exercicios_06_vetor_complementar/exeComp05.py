"""
Escrever um programa em Python que leia um vetor V1 de n posições e gere um vetor
V2 de tamanho n que é o vetor V1 invertido.
"""
import random

tam = int(input('Digite o tamanho do vetor: '))
v1 = [None]*tam
v2 = [None]*tam

for i in range(tam):
    v1[i] = random.randint(0,9)

# Para inverter o vetor
for e in range(tam):
    v2[tam-1-e] = v1[e]

print('V1 =',v1)
print('V2 =',v2)
