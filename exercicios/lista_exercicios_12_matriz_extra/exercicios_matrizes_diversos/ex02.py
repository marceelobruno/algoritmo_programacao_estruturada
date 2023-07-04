"""
https://www.galirows.com.br/meublog/programacao/exercicios-simples-com-matrizes/

Dada uma matriz de inteiros A(mxn), verificar se existem elementos repetidos em A.
"""
# ordem da matriz
m = int(input('Informe o n° de linhas: '))
n = int(input('Informe o n° de colunas: '))

# criando a matriz usando list comprehension
mat = [[None for j in range(n)]for i in range(m)]

# vetor que receberá todos os elementos da matriz
vet = []

# contador de elementos repetidos
cont = 0

# preenchendo a matriz
print('\nPreencha a matriz:')
for i in range(m):
    for j in range(n):
        mat[i][j] = int(input('Elemento: '))
        vet.append(mat[i][j])

# exibindo a matriz
print('\nMatriz:')
for i in range(m):
    for j in range(n):
        print(f'{mat[i][j]:4}', end=' ')
    print()

# conferindo se há elemento repetido
for i in vet:
    if vet.count(i) > 1:
        cont += 1

# conferindo contagem de elemento repetido da matriz
if cont != 0:
    print('\nHá elemento repetido na matriz')
else:
    print('\nNão há elemento repetido na matriz')
