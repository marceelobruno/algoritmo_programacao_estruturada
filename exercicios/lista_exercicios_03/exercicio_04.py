"""Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a
mensagem "Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa.

OBS: Fulano e Fulana são nomes exemplos."""

# nome = input('Digite seu nome: ').title()
# sexo = input('Digite o seu sexo - M ou F: ')


# if sexo == 'M' or sexo == 'm':
#     print(f'Olá, Sr. {nome}!')

# elif sexo == 'F' or sexo == 'f':
#     print(f'Olá, Sra. {nome}!')

# else:
#     print(f'{nome}, você informou um tipo de sexo não existente.')


# Using PEP 636 – Structural Pattern Matching
# https://peps.python.org/pep-0636/

nome = input('Digite seu nome: ').title()
sexo = input('Digite o seu sexo - M ou F: ')

match sexo:
    case 'M' | 'm':
        print(f'Olá, Sr. {nome}!')

    case 'F' | 'f':
        print(f'Olá, Sra. {nome}!')

    # case _:
    case other:
        print(f'{nome}, você informou um tipo de sexo desconhecido.')
