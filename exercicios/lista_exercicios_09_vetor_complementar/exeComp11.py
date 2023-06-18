"""
Elabore um algoritmo que leia 10 valores e em seguida mostre todos os valores
pares ou múltiplos de 5. Também mostre quantos valores ímpares e negativos existem.
Ao final, mostre todos os valores negativos digitados, na ordem contrária em que foram informados.

v = [1, -1, 2, 3, -5, -7, -9, 100, 15, 20]
Valores pares ou múltiplos de 5 do Vetor: [2, 100, 15, 20].
Negativos invertidos: [-9, -7, -5, -1]
"""
n = 10
cont = 0
v = []
par_mult = []
neg_v = []
neg_for = []
v = [1, -1, 2, 3, -5, -7, -9, 100, 15, 20]
# print(f'Informe {n} números: ')
# while len(v) < n:
#     num = int(input())
#     v.append(num)

for i in range(n):
    if (v[i] % 2 == 0 or v[i] % 5 == 0) and v[i] > 0:
        par_mult.append(v[i])
    elif v[i] % 2 == 1 or v[i] < 0:
        cont += 1
        if v[i] < 0:
            neg_v.append(v[i])

neg_orig = neg_v
print('Neg =', neg_orig)

neg_v.reverse()

print(f'Valores pares ou múltiplos de 5 do Vetor: {par_mult}.')
print(f'Quantidade valores ímpares e negativos do vetor: {cont}.')

if len(neg_v) > 0:
    print(f'Negativos invertidos: {neg_v}')
else:
    print('Não há números negativos no vetor.')
