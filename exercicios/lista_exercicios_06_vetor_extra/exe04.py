"""
4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também
dois valores X e Y quaisquer correspondentes a duas posições no vetor.
Ao final, seu programa deverá escrever a soma dos valores encontrados nas
respectivas posições  X e Y .
"""
tam = 8
a = [None] * tam
soma = 0

print(f'Informe {tam} valores:')
for i in range(tam):
    a[i] = int(input())

x = int(input(f'Informe um número entre 0 e {tam-1}: '))
y = int(input(f'Informe outro número entre 0 e {tam-1}: '))

for e in range(tam):
    if a[e] == a[x]:
        soma += a[e]
    if a[e] == a[y]:
        soma += a[e]

print('Vetor A =', a)
print(f'O resultado dos valores encontrados nas respectivas posições {x} e {y}: {soma}.')
