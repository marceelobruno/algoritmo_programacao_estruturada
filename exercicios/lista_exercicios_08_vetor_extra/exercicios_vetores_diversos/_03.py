"""
http://www.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

3. Ler um vetor de 10 elementos inteiros e positivos.
Criar um segundo vetor da seguinte forma:

Elementos de índice par receberão os respectivos elementos divididos por 2;
Elementos de índice ímpar receberão os respectivos elementos multiplicados por 3.
Imprima os dois vetores.
"""
# tamanho dos vetores
tam = 5

# criando os vetores
vet_a = []
vet_b = []

cont = 0

# preenchendo o vetor a
print('Informe os valores:')
while True:
    num = int(input())
    if num < 0:
        print('Número negativo! Tente novamente.')
    else:
        vet_a.append(num)
        cont += 1
    if cont == tam:
        break

# preenchendo o vetor b
for i in range(tam):
    if i % 2 == 0:
        vet_b.append(vet_a[i] // 2)
    else:
        vet_b.append(vet_a[i] * 3)

# imprimindo os vetores
print(f'''Vetor A: {vet_a}\nVetor B: {vet_b}''')
