"""
8. Crie um programa que leia 6 valores inteiros e, em seguida,
mostre na tela os valores lidos na ordem inversa.
"""
tam = 6
x = [None]*tam
y = [None]*tam

print(f'Informe {tam} valores para o vetor:')
for i in range(tam):
    x[i] = int(input())
    for j in range(tam):
        y[tam-1-j] = x[j]
        continue

print('Vetor original =',x)
print('Vetor original invertido =',y)
