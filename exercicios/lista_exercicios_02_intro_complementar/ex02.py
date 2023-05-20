PESO_1 = 6.0
PESO_2 = 4.0

primeira_nota = float(input('Informe a primeira nota: '))
segunda_nota = float(input('Informe a segunda nota: '))

media_ponderada = (primeira_nota * PESO_1 + segunda_nota * PESO_2) / 10.0

print(f'A média ponderada das notas informadas é {media_ponderada:.2f}')
