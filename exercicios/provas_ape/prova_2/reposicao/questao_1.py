# tamanho do vetor
n = int(input('Tamanho do vetor: '))

# criando vetores
vet_a = [None] * n
vet_b = [None] * n

print('\nPreencha o vetor A:')
for i in range(n):
    vet_a[i] = int(input(f'{i+1}° Elemento: '))
    if i % 2 == 0:
        vet_b[i] = vet_a[i] * 2
    else:
        vet_b[i] = vet_a[i] * 3

# exibindo vetor b
print('\nVetor B:', vet_b)
