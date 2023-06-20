"""
3. Declare uma matriz 5 x 5. Preencha com 0 a diagonal secundária e com 1 os demais
elementos. Exiba ao final a matriz obtida.
"""
ordem = 5
mat = [[None]*ordem for i in range(ordem)]

print('Matriz')
for i in range(ordem):
    for j in range(ordem):
        if i+j == ordem-1:
            mat[i][j]=0
        else:
            mat[i][j]=1
        print(f'{mat[i][j]:4}',end=' ')
    print()
