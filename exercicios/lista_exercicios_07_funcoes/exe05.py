"""
Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua
média e seu conceito.
O programa deve conter as seguintes funções:
• Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua
média (aritmética).
• Uma função que receba como parâmetro a média do aluno e retorne o seu
conceito, de acordo com a tabela abaixo:

MÉDIA       CONCEITO
8,0  >=           A
5,0 e <= 8,0     B
< 5,0           C
"""

def media(n1,n2,n3):
    return (n1+n2+n3)/3

def conceito(media):
    if media>=8:
        return 'A'
    elif media>=5:
        return 'B'
    else:
        return 'C'

# Programa Principal

nota1 = float(input('Escreva sua 1ª nota: '))
nota2 = float(input('Escreva sua 2ª nota: '))
nota3 = float(input('Escreva sua 3ª nota: '))

med = media(nota1,nota2,nota3)
print(f'Média: {med:.2f} e conceito: {conceito(med)}')