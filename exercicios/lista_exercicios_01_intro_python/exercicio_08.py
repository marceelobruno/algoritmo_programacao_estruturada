"""
8 - Faça um programa que leia o nome de um aluno e as notas das três provas que
ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).
"""

aluno = input('Informe o nome do aluno: ')

primeira_nota = float(input('Digite o valor da primeira nota: '))
segunda_nota = float(input('Digite o valor da segunda nota: '))
terceira_nota = float(input('Digite o valor da terceira nota: '))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print(f'A média do aluno {aluno}, é: {media:.2f}')
