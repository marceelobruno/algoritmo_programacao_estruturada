"""
2 - Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas.
Sabe-se que nota1 possui peso 6 e nota2 possui peso 4.
"""

PESO_NOTA_1 = 6
PESO_NOTA_2 = 4

primeira_nota = float(input('Qual a primeira nota: '))
segunda_nota = float(input('Qual a segunda nota: '))

media = (primeira_nota * PESO_NOTA_1 + segunda_nota * PESO_NOTA_2) / (PESO_NOTA_1 + PESO_NOTA_2)

print(f'A média ponderada para as notas informadas é {media}')
