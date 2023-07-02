"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

9. Faça um programa para ler uma quantidade N de números inteiros e armazená-los
em um vetor. O programa deve trocar o menor elemento do vetor com o elemento da
primeira posição, e imprimir o vetor resultante.
"""
n = 7
vet = []

# Preenchendo o vetor
print(f'Informe {n} elementos:')
for i in range(n):
    # vet[i] = int(input(f'{i+1}° elemento: '))
    vet.append(int(input(f'{i+1}° elemento: ')))

menor = vet[0]

# Verificando qual elemento é o menor
for i in range(n):
    if vet[i] < menor:
        menor = vet[i]

index = vet.index(menor)

# Exindo o vetor antes da troca
print('\nVetor Inicial: ', vet)

# Trocando posições dos elementos
for i in range(n):
    if i == 0:
        vet[index] = vet[i]
        vet[i] = menor

# Exindo o resultado
print('Vetor Resultante: ', vet)
