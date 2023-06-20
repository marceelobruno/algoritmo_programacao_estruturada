"""
4. Escreva uma função chamada soma que receba um vetor e retorne a soma dos
seus elementos (obs: não use a função sum). 
Escreva também um programa que, dado o vetor V = [ 6,3,8,7,2,5 ] e usando a
função soma criada, informe a soma dos elementos do vetor V.
"""

def soma(vetor):
    total = 0
    for elemento in vetor:
        total +=elemento
    return total

V = [6,3,8,7,2,5]

print(soma(V))