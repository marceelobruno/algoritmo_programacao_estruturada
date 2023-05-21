# Solicitar N números do usuário, verificar e exibir se o número lido é par ou ímpar

iterador = 1
quantidade = int(input('Informe a quantidade de números: '))

while iterador <= quantidade:
    numero = int(input(f'{iterador}º - Informe um outro número: '))
    if numero % 2 == 0:
        print(f'{numero} é par.')
    else:
        print(f'{numero} é ímpar.')
    iterador += 1
