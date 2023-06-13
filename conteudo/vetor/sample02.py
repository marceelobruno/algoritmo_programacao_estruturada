N = 5
v = [None] * N
somador = 0
media = 0
print('Informe ', N, ' números inteiros: ')
for i in range(N):
    v[i] = int(input())
    somador += v[i]

media = somador / N

print(f'A soma dos números: {somador}. A média: {media}. Os números acima da média: ', end=' ')
for j in v:
    if j > media:
        print(j, end=', ')
