"""
1. Escreva um programa que solicite a digitação de um número (de 1 a 7)
correspondente a um dia da semana e imprima o nome do dia da semana e se é dia
útil (de segunda a sexta) ou final de semana (sábado e domingo). 
OBS: Considere que o dia 1 é o domingo.
"""

dia_da_semana = int(input('Informe um número de 1 a 7: '))

if dia_da_semana == 1:
    print('Domingo. Final de semana.')

elif dia_da_semana == 2:
    print('Segunda. Dia útil.')

elif dia_da_semana == 3:
    print('Terça. Dia útil.')

elif dia_da_semana == 4:
    print('Quarta. Dia útil.')

elif dia_da_semana == 5:
    print('Quinta. Dia útil.')

elif dia_da_semana == 6:
    print('Sexta. Dia útil.')

elif dia_da_semana == 7:
    print('Sábado. Final de semana.')

else:
    print('Você informou um número fora do escopo. Tente novamente!')
