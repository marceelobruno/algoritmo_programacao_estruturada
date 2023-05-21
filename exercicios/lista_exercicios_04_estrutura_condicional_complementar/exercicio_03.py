"""
3 - Escreva um programa que solicite a digitação de um ano e imprima sua 
classificação como bissexto ou não bissexto.
OBS: um ano é bissexto se for divisível por 4, mas não por 100.
Um ano também é bissexto se for divisível por 400.
"""

ano = int(input('Informe um ano com 4 digítos: '))

if ano % 2 == 0:
    print(f'{ano} é bissexto.')
else:
    print(f'{ano} não é bissexto.')
