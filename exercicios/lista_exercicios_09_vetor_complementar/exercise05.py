"""
5. Faça um programa para ler as 8 dezenas apostadas por 20 apostadores e
verificar se a aposta é válida (cada dezena está entre [1, 80] e não pode haver
repetição). O programa deverá calcular e exibir a quantidade de números
acertados em cada aposta. Atenção! As dezenas sorteadas são: 06, 07, 13, 14 e 26.
"""

# Número de apostadores (testando p/ apenas 3 apostadores ao invés de 20)
num_apostadores = 2

# Número de dezenas apostadas por cada apostador
num_dezenas_apostadas = 8

# Vetor que irá conter as dezenas apostadas por um apostador
vet_das_apostas = [None] * num_dezenas_apostadas

# Vetor que contém as dezenas sorteadas
vet_dezenas_sorteadas = [6, 7, 13, 14, 26]

# Número de dezenas sorteadas
nds = len(vet_dezenas_sorteadas)

for i in range(num_apostadores):

    # Lendo as dezenas de um apostador
    print(f'\nDezenas do {i+1}° Apostador:')
    for j in range(num_dezenas_apostadas):
        vet_das_apostas[j] = int(input())

    # Verificando se a aposta é válida
    valida = True
    for dezena in vet_das_apostas:
        if dezena < 1 or dezena > 80 or vet_das_apostas.count(dezena) > 1:
            valida = False
            break

    # Contando a quantidade de acertos se a aposta for válida
    if valida:
        cont = 0
        for dezena in vet_das_apostas:
            if dezena in vet_dezenas_sorteadas:
                cont += 1
        print(f'Número de acertos: {cont}')
    else:
        print('Aposta inválida!')
