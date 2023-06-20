"""
5. Escreva um programa que:
a) Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de
uma turma e a média de cada um deles.
    o As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
    o As médias serão calculadas e armazenadas na 4a coluna da matriz.
b) Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
c) Calcule e imprima a média geral da turma.
d) Calcule e imprima o número de alunos com média superior à média geral da turma.
"""

#criação da matriz
na = 2
nn = 3
mat = [[None]*(nn+1) for i in range(na)]

#leitura das notas
print('Digita as notas dos alunos')
for i in range(na):
    print(f'\n{i+1}º ALUNO:')
    for j in range(nn):
        mat[i][j] = float(input(f'{j+1}ª Nota: '))

#cálculo das médias
for i in range(na):
    mat[i][nn] = (mat[i][0] + mat[i][1] + mat[i][2]) / nn

#impressão da matriz
print('\n          1ª NOTA   2ª NOTA   3ª NOTA    MÉDIA')
for i in range(na):
    print(f'{i+1}º ALUNO',end='')
    for j in range(nn+1):
        print(f'{mat[i][j]:9.1f}',end='')
    print()

#cálculo da média geral da turma
soma = 0
for i in range(na):
    soma += mat[i][nn]
media = soma / na
print(f'\nMédia geral da turma: {media:.1f}')

#cálculo do número de alunos com média superior à média geral da turma
cont = 0
for i in range(na):
    if mat[i][nn] > media:
        cont += 1
print(f'\nNúmero de alunos com média superior à média geral da turma: {cont}')
