"""
https://www.galirows.com.br/meublog/programacao/exercicios-resolvidos-python/

Exercício 3: Faça um algoritmo que solicite ao usuário números e os armazene 
em um vetor de 20 posições. Crie uma função que recebe o vetor preenchido e
substitua todas as ocorrências de valores negativos por zero, as ocorrências
de valores menores do que 10 por 1 e as demais ocorrências por 2.
"""


def transforma_vetor(tam: int, vetor: list) -> list:
    for i in range(tam):
        if vetor[i] < 0:
            vetor[i] = 0
        elif vetor[i] < 10:
            vetor[i] = 1
        else:
            vetor[i] = 2
    return vetor


n = 20
vet = [None] * n

# preenchendo o vetor
for i in range(n):
    vet[i] = int(input(f'Informe o elemento {i+1}: '))

print('\nVetor original:', vet)
print('Vetor transformado:', transforma_vetor(n, vet))
