"""
5 - Escreva um programa para ler o nome e o sobrenome de uma pessoa e escrevê-
los na seguinte forma: sobrenome seguido por uma vírgula e pelo nome
"""

primeiro_nome = input('Digite o seu primeiro nome: ')
sobrenome = input('Digite o seu sobrenome: ')

print(f'Usuário: {sobrenome},'.title(), f' {primeiro_nome}'.title())
