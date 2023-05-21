"""
8 - Escreva um programa que tenha a funcionalidade de uma calculadora simples.
O programa deve solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir "Operador desconhecido".
"""

number_1 = int(input('Digite o primeiro número: '))
number_2 = int(input('Digite o segundo número: '))
operador = input('Escolha apenas um dos seguintes operadores: + - * / %: ')

match operador:
    case '+':
        print(f'Resultado: {number_1 + number_2}')
    case '-':
        print(f'Resultado: {number_1 - number_2}')
    case '*':
        print(f'Resultado: {number_1 * number_2}')
    case '/':
        print(f'Resultado: {number_1 / number_2:.0f}')
    case '%':
        print(f'Resultado: {number_1 % number_2}')
    case _:
        print('Operador desconhecido.')
