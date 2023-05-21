"""
2. Escreva um programa que solicite a digitação de um caractere qualquer do
teclado e imprima sua classificação: vogal, consoante, número e caractere especial.
"""

caractere = input('Digite um caractere: ').upper()

if caractere >= 'A' and caractere <= 'Z':
    if caractere in ('A', 'E', 'I', 'O', 'U'):
        tipo = 'vogal'
    else:
        tipo = 'consoante'
else:
    if caractere >= '0' and caractere <= '9':
        tipo = 'número'
    else:
        tipo = 'caractere especial'
print('Caractere do tipo: ',tipo)
