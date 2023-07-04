import random

# ordem da matriz
tam = 2

# criando a matriz
mat = [[None] * tam for i in range(tam)]

# variável de verificação
identidade = True

# preenchendo e verificando a matriz
for i in range(tam):
    for j in range(tam):
        mat[i][j] = random.randint(0, 1)
        if i == j and mat[i][j] != 1:
            identidade = False
        elif i != j and mat[i][j] != 0:
            identidade = False

# verificando e exibindo a variável identidade
if identidade:
    print('Matriz Identidade.')
else:
    print('Não é Matriz Identidade.')
