"""
http://www.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

2. Ler um vetor de 10 elementos. Crie um segundo vetor, com todos os elementos
na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo
será o segundo e assim por diante. Imprima os dois vetores.
"""
from random import randint

tam = 5
vet_a = [None] * tam
vet_b = [None] * tam

# preenchendo vetor a
for i in range(tam):
    vet_a[i] = randint(1, 20)

# preenchendo vetor b com a ordem inversa do vetor a
for i in range(tam):
    vet_b[i] = vet_a[tam - 1 - i]

# imprimindo vetores
print('Vetor A: ',vet_a)
print('Vetor B: ',vet_b)
