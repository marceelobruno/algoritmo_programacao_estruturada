"""
https://www.galirows.com.br/meublog/programacao/exercicios-resolvidos-python/

Exercício 1: faça um algoritmo que solicite ao usuário números e os armazene em
um vetor de 30 posições. Crie uma função que recebe o vetor preenchido e substitua
todas as ocorrência de valores positivos por 1 e todos os valores negativos por 0.
"""


def transformandoVetor(tamanho: int, vetor: list) -> list:
    for i in range(tamanho):
        if vetor[i] >= 0:
            vetor[i] = 1
        else:
            vetor[i] = 0
    return vetor


n = 30
vet = [None] * n

print('Preenchendo o vetor:')
for i in range(n):
    vet[i] = int(input())

print('Vetor Original:', vet)
print('Vetor Modificado:', transformandoVetor(n, vet))
