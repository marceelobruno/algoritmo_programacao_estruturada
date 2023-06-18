"""
5 - Faça um programa que, para um grupo de N pessoas (obs: N será lido):
i. Leia o sexo (M ou F) de cada pessoa;
ii. Calcule e escreva o percentual de homens;
iii. Calcule e escreva o percentual de mulheres.
"""
contMasc = 0
contFem = 0
pessoas = int(input('Informe a quantidade de pessoas: '))

for p in range(pessoas):
    sexo = input('Informe o seu sexo - M ou F: ').upper()

    if sexo == 'M':
        contMasc += 1
    elif sexo == 'F':
        contFem += 1
    else:
        print('Sexo não específicado')
percMasc = contMasc / pessoas * 100
percFem = contFem / pessoas * 100

print(f'Porcentagem de homens {percMasc:.0f}% e mulheres {percFem:.0f}%.')
