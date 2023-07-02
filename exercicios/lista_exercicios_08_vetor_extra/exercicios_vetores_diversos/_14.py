"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

03. Faça um programa cujas entradas são o número de elementos de um vetor de
números inteiros, seguida dos elementos do vetor, seguido de um valor a ser
procurado no vetor. O programa deve retornar um número inteiro indicando o 
índice da posição do elemento, caso ele tenha sido encontrado, ou o número -1,
caso não tenha sido encontrado.
"""
tam = int(input('Tamanho: '))
procurado = int(input('Elemento procurado: '))
vet = [None] * tam

for i in range(tam):
    vet[i] = int(input(f'Informe o {i+1}° elemento: '))

if procurado not in vet:
    print(f'\nPosição do elemento {procurado}: -1')
else:
    print(f'\nPosição do elemento {procurado}: {vet.index(procurado)}')
