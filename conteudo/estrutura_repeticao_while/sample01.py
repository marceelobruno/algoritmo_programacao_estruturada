"""
Faça um programa que solicite do usuário vários números até que seja informado o número 0.
Sempre que o usuário informar um número o programa deverá mostrar o dobro desse número.
"""

numero = int(input('Informe um número inteiro: '))

while numero != 0:
    print(f'O dobro de {numero} é {numero*2}.')
    numero = int(input('Informe outro número inteiro: '))

print('\nVocê encerrou o programa ao informar o número 0.')
