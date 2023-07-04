"""
http://www.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

6. Faça um programa que deverá permitir que o usuário entre com os valores
dos elementos de uma matriz quadrada de ordem 4 e possibilite o usuário
realizar as seguintes funcionalidades:
a) Imprimir todos os elementos da matriz;
b) Somar os quadrados de todos os elementos da primeira coluna;
c) Somar todos os elementos da terceira linha;
d) Somar os elementos da diagonal principal; e
e) Somar todos os elementos de índice par da segunda linha.
"""
# FIXME

# Função para imprimir uma matriz
def printa(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(f'{matriz[i][j]:4}', end=' ')
        print()


def quadrados(matriz):
    soma = 0
    for j in range(len(matriz)):
        for i in range(len(matriz)):
            if j == 0:
                soma += matriz[i]
    return soma


def terceiraLinha(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == 2:
                soma += matriz[i][j]
    return soma


# Função para imprimir a diagonal principal da matriz
def diagonalPrincipal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                soma += matriz[i][j]
    return soma


def somaPar(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == 1:
                if j == 0 or j == 3:
                    soma += matriz[i][j]
    return soma


# Programa Principal
ordem = 4

# Criando a matriz
mat = [[None] * ordem for i in range(ordem)]

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# Preenchendo a matriz
print('Preencha a matriz:')
for i in range(ordem):
    for j in range(ordem):
        matriz = m[i][j]


while True:
    print('''
Escolha entre as opções abaixo ou digite 0 para sair do programa:
    a) Imprimir todos os elementos da matriz;
    b) Somar os quadrados de todos os elementos da primeira coluna;
    c) Somar todos os elementos da terceira linha;
    d) Somar os elementos da diagonal principal; e
    e) Somar todos os elementos de índice par da segunda linha.\n''')

    opcao = input('Opção: ').lower()

    if opcao == '0':
        break
    print()

    if opcao == 'a':
        printa(m)
    elif opcao == 'b':
        print(quadrados(m))
    elif opcao == 'c':
        print(terceiraLinha(m))
    elif opcao == 'd':
        print(diagonalPrincipal(m))
    elif opcao == 'e':
        print(somaPar(m))
    else:
        print('Opção inválida! Tente novamente...')
