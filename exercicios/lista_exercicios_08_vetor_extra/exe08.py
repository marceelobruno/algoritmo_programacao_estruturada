"""
9. Crie um programa que receba 6 valores inteiros pares e, em seguida,
mostre na tela os valores lidos na ordem inversa.
"""
tam = 6
x = []
y = [None]*tam

print(f'Informe {tam} valores: ')
while len(x) < tam:
    num = int(input())
    if num % 2 == 0:
        x.append(num)
    else:
        print('Informe um número par!')

print('Vetor original =', x)

for i in range(tam):
    y[tam - 1 - i] = x[i]

print('Vetor invertido =', y)
