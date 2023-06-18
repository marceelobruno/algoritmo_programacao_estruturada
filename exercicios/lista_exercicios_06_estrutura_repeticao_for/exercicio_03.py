"""
3 - Faça um programa que calcule e mostre o fatorial de um número N, fornecido
pelo usuário. A definição de fatorial é mostrada a seguir:
"""

numero = int(input('Informe um número inteiro: '))

fatorial = 1

for i in range(2, numero+1):
    fatorial *= i

print(f'Resultado do fatorial {numero}!: {fatorial}')
