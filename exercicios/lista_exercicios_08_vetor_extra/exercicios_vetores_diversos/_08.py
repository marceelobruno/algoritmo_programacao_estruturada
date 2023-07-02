"""
https://www.ime.usp.br/~macmulti/exercicios/vetores/index.html

8. Dados dois vetores x e y, ambos com N elementos,
determinar o produto escalar (1) desses vetores.
Fórmula do produto escalar: u.v = a.c + b.d
"""
from random import randint

tam = 2
produto = 0
vet_a = []
vet_b = []

# preenchendo os vetores
for i in range(tam):
    num = randint(-5,20)
    vet_a.append(num)
    num2 = randint(-5,20)
    vet_b.append(num2)

# calculando o produto escalar
for i in range(tam):
    produto += vet_a[i] * vet_b[i]

# Imprimindo os vetores e o resultado do produto escalar
print(f'''
Vetor A: {vet_a}
Vetor B: {vet_b}
Produto Escalar: {produto}''')
