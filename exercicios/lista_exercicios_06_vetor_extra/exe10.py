"""
12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a média dos valores.
"""
tam = 5
x = [None] * tam

print(f'Preencha {tam} elementos para o vetor:')
for i in range(tam):
    x[i] = int(input())

menor = min(x)
posMenor = x.index(menor)
maior = max(x)
posMaior = x.index(maior)
media = sum(x) / tam

print('Elementos do vetor:', x)
print('Média dos elementos do vetor:', media)

# 13. mostrando a posição onde se encontram o maior e o menor valor.
print(f'Menor elemento do vetor: {menor} encontra-se no índice {posMenor}')
print(f'Maior elemento do vetor: {maior} encontra-se no índice {posMaior}')
