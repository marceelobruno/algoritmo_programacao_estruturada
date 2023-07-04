"""
69. Escreva um programa que leia um vetor de 15 posições de inteiros.
Em seguida, o programa deve ler um valor inteiro e imprimir o número
de vezes que este valor ocorre no vetor.
"""
# tamanho do vetor
tam = 10

# criando o vetor
vet = [None] * tam

# número desejado
num = int(input('Informe um número: '))

# variável para contar a quantidade de ocorrências
cont = 0

# preenchendo o vetor
for i in range(tam):
    vet[i] = int(input(f'{i+1}° elemento: '))
    if vet[i] == num:
        cont += 1

# exibindo os resultados
print(f'Vetor: {vet}\nO número {num} ocorre {cont} vez(es) no vetor.')
