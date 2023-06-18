"""
24. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
o número do aluno e o segundo representando a sua altura em metros.
Encontre o aluno mais baixo e o mais alto.
Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.
"""
n = 4
aluno = [None]*n
altura = [None]*n

print('Informe o número do aluno e sua altura:')
for i in range(n):
    print(f'\nDigite o número do {i+1}° aluno:',end=' ')
    aluno[i] = int(input())
    print('Agora digite a sua altura:',end=' ')
    altura[i] = float(input())

menorAlt = altura[0]
maiorAlt = altura[0]
for j in range(n):
    if altura[j] > maiorAlt:
        maiorAlt = altura[j]
    elif altura[j] < menorAlt:
        menorAlt = altura[j]

posMenor = altura.index(menorAlt)
posMaior = altura.index(maiorAlt)

print(f'\nO aluno {aluno[posMenor]} é o mais baixo com {menorAlt}cm.')
print(f'O aluno {aluno[posMaior]} é o mais alto com {maiorAlt}cm.')
