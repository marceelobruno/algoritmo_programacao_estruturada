"""
Faça um programa que, leia a temperatura dos 30 dias do mês de Abril diga
qual o dia mais quente e o dia mais frio do mês.
obs: suponha que não haja empates.
"""

DIAS = 4

temp_dia_quente = -100
temp_dia_frio = 100

for dia in range(1,DIAS+1):
    temperatura = int(input(f'Informe a temperatura do {dia}º dia: '))

    if temperatura < temp_dia_frio:
        temp_dia_frio = temperatura
        dia_frio = dia

    if temperatura > temp_dia_quente:
        temp_dia_quente = temperatura
        dia_quente = dia

print(f'''
Dia mais frio do mês: {dia_frio}, {temp_dia_frio}º C
Dia mais quente do mês: {dia_quente}, {temp_dia_quente}º C
      ''')
