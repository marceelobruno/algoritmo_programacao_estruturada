"""
5. Leia um vetor de 10 posições.
Conte e escreva quantos valores pares ele possui.
"""
tam = 10
x = [None] * tam
cont = 0
par = []

print(f'informe {tam} elementos:')
for i in range(tam):
    x[i] = int(input())
    if x[i] % 2 == 0:
        par.append(x[i])
        cont += 1
print('Vetor X:', x)

if cont > 0:
    print(f'O vetor possui {cont} elemento(s) par(es): {par}')
else:
    print('Não há elemento par no vetor X')
