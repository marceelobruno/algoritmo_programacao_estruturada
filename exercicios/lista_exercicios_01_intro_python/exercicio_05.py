"""
5 - Escreva um programa para ler o nome e o sobrenome de uma pessoa e escrevê-
los na seguinte forma: sobrenome seguido por uma vírgula e pelo nome
"""

primeiro_nome = input('Digite o seu primeiro nome: ').title()
sobrenome = input('Digite o seu sobrenome: ').title()

print(f'{sobrenome}, {primeiro_nome}')
