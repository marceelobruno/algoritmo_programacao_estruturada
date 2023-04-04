# estudante = input('Digite seu nome: ').title()
# conceito = input('Digite seu conceito: ').title()

# if conceito == 'A':
#     print(f'Olá, {estudante}. O seu status de recomendação é: Fortemente Recomendado.')

# elif conceito == 'B' or conceito == 'C':
#     print(f'Olá, {estudante}. O seu status de recomendação é: Recomendado.')

# elif conceito == 'D':
#     print(f'Olá, {estudante}. O seu status de recomendação é: Não Recomendado.')

# else:
#     print(f'{estudante}, você informou um conceito fora do esperado.')


# Structural Pattern Matching
estudante = input('Digite seu nome: ').title()
conceito = input('Digite seu conceito: ').title()

match conceito:
    case 'A':
        print(f'Olá, {estudante}. O seu status de recomendação é: Fortemente Recomendado.')

    case 'B' | 'C':
        print(f'Olá, {estudante}. O seu status de recomendação é: Recomendado.')

    case 'D':
        print(f'Olá, {estudante}. O seu status de recomendação é: Não Recomendado.')

    case _:
        print(f'{estudante}, você informou um conceito fora do esperado.')
