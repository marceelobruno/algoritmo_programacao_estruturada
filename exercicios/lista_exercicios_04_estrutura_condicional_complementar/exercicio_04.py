"""
4 - Escreva um programa que leia a hora de início de um jogo e a hora do final
do jogo (considerando apenas horas inteiras), calcula a duração do jogo em horas,
sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode
iniciar em um dia e terminar no dia seguinte.
O programa deve mostrar o resultado obtido.
"""

hora_inicio = int(input('Que horas o jogo começou: '))
hora_fim = int(input('Que horas o jogo terminou: '))

if hora_inicio < hora_fim:
    tempo = hora_fim - hora_inicio
else:
    tempo = 24 - hora_inicio + hora_fim
print(f'O jogo durou {tempo} hora(s).')
