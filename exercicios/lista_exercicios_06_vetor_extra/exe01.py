"""
https://www.facom.ufu.br/~backes/gci007/ListaC04.pdf
https://www.andrebackes.com/listas/e0ffdc9b-285a-4b32-976b-7341e6d6bc06

1. Faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
O programa deve executar os seguintes passos:
(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variável inteira (simples) a soma entre os valores das posições:
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
"""
tam = 6
a = [None] * tam
a = [1, 0, 5, -2, -5, 7]
somaA = []

print('A =', a)
for i in range(tam):
    if a[i] == a[0]:
        somaA.append(a[i])
    if a[i] == a[1]:
        somaA.append(a[i])
    if a[i] == a[5]:
        somaA.append(a[i])

print('Soma A:', somaA)

soma = sum(somaA)
print('A soma dos elementos do vetor nos índices (0, 1 e 5) é foi:', soma)

for e in range(tam):
    if a[e] == a[4]:
        a[e] = 100
    print(a[e])
