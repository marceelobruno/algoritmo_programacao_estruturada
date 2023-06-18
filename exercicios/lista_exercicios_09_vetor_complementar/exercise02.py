"""
2. Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão
lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a
intercalação dos elementos de A e B.
Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]
"""
from random import randint

#leitura do tamanho do vetor
# n = int(input('Digite o tamanho do vetor: '))
n=3

#inicialização dos vetores A, B e C
a = [None] * n
b = [None] * n
c = [None] * (n * 2)

#geração do vetor A
print('Informe os elementos do vetor A: ')
for i in range(n):
    # a[i] = int(input())
    a[i] = randint(1,20)
print('A = ',a)

#geração do vetor B
print('Informe os elementos do vetor B: ')
for i in range(n):
    b[i] = randint(21,40)
print('B = ',b)

#geração do vetor C
for i in range(n):
    c[i*2] = a[i]
    c[i*2+1] = b[i]
print('C = ',c)
