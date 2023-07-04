"""
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjTotK99vD_AhUZnpUCHZQSDDUQFnoECA0QAQ&url=https%3A%2F%2Fads.ifba.edu.br%2Fdl1012&usg=AOvVaw2G6gRZqERxw6Z4Hff7240o&opi=89978449

67. Faça um programa em C que leia dois vetores de 10 posições de inteiros
e copie o maior valor dos dois em cada posição em um terceiro vetor.
Em seguida, imprima este terceiro vetor.
"""
import random

# tamanho dos vetores
tam = 10

# criando os vetores
vet_a = [None] * tam
vet_b = [None] * tam
vet_c = [None] * tam

# preenchendo os vetores
for i in range(tam):
    vet_a[i] = random.randint(1, 30)
    vet_b[i] = random.randint(1, 30)

    if vet_a[i] > vet_b[i]:
        vet_c[i] = vet_a[i]
    else:
        vet_c[i] = vet_b[i]

# imprimindo os vetores
print(f'Vetor A: {vet_a}\nVetor B: {vet_b}\nVetor C: {vet_c}')
