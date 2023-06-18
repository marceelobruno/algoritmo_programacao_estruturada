"""
2. Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.
"""
# Tamanho do vetor
tam = 5
cont = 0

# Iniciando o vetor V
v = [None]*tam
# Lendo os elementos do vetor V
for i in range(tam):
    v[i] = int(input(f'V[{i}]: '))

# Leitura do valor K
k = int(input('Informe um valor para "K": '))

for i in range(tam):
    if v[i] == k:
        cont+=1

print(f'Quantidade de ocorrências do número {k} dentro do vetor V: {cont}')
