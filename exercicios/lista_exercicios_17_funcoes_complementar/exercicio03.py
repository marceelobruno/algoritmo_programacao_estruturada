"""
3. Escreva um programa que leia N números inteiros (máximo 20) e armazene em um
vetor X. Calcule a média dos elementos do vetor e informe quantos elementos
estão abaixo da média do conjunto.

Crie as seguintes funções:
• Uma função que faça a leitura dos elementos de um vetor de inteiros.
Essa função deve receber como parâmetro o número de elementos do vetor e deve
retornar o vetor preenchido;
• Uma função que calcule a média dos elementos de um vetor. Essa função deve
receber como parâmetro um vetor e retornar a média dos elementos dele;
• Uma função que receba um vetor e um número, e retorne quantos elementos do
vetor estão abaixo desse número.
"""

# Função para ler um vetor


def ler_vetor(qtd):
    vetor = [None] * qtd
    for i in range(qtd):
        vetor[i] = int(input())
    return vetor


# Função para calcular a média de um vetor
def media_vetor(vetor):
    return sum(vetor) / len(vetor)


# Função para contar os elementos abaixo da média
def cont_vetor(vetor, med):
    cont = 0
    for elem in vetor:
        if elem < med:
            cont += 1
    return cont


# Programa principal
tam = 5  # Testando com apenas 5 elementos
print(f'Digite os {tam} elementos do vetor:')
vet = ler_vetor(tam)
med = media_vetor(vet)
conta_vet = cont_vetor(vet, med)
print(f'A média do elementos do vetor é: {med:.1f}')
print(f'Existe(m) {conta_vet} elemento(s) abaixo da média')
