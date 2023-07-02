"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

08. Palíndrome é uma palavra que pode ser lida tanto da esquerda para a direita
como da direita para a esquerda, resultando na mesma sequência de caracteres.
Faça um programa que lê uma palavra e verifica se a mesma é palíndrome ou não.
Exemplo:
Digite uma palavra: arara
arara é palíndrome
"""
palavra = input('Digite uma palavra: ')
palavra_reverse = ''

for i in palavra:
    palavra_reverse += i

if palavra == palavra_reverse:
    print(f'{palavra_reverse} é palíndrome')
else:
    print('Não é palíndrome')
