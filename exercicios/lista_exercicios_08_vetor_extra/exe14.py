"""
17. Leia um vetor de 10 posições e atribua valor 0 para todos os elementos
que possuírem valores negativos.
"""
tam = 5
v = [None] * tam

print(f'Informe {tam} elementos para o vetor V:')
for i in range(tam):
    v[i] = int(input())
    if v[i] < 0:
        v[i] = 0

print('Valores do vetor V =', v)
