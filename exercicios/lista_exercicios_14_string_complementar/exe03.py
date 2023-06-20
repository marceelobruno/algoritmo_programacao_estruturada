"""
3. Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo abaixo.
OBS: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.
Exemplo:
Entrada: FLAVIO RIBEIRO COUTINHO
Saída: COUTINHO, F. R.
"""
nome = input('Nome Completo: ').upper().split()
tam = len(nome)
saida = nome[-1] + ', '

for i in range(tam - 1):
    saida += nome[i][0] + '. '

print(saida)
