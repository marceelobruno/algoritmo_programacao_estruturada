"""
http://www.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

4. Ler um vetor com 10 nomes de pessoas, após pedir que o usuário
digite um nome qualquer de pessoa.
Escrever a mensagem “ACHEI”, se o nome estiver armazenado no vetor C
ou “NÃO ACHEI” caso contrário.
"""
tam = 10
nomes = [None] * tam

# preenchendo vetor com diversos nomes
for i in range(tam):
    nomes[i] = input(f'Informe o {i + 1}° nome: ')

# buscando o nome no vetor
while True:
    tentativa = input('\nEscolha um nome: ')
    if tentativa in nomes:
        print('ACHEI!')
        break
    print('\nNÃO ACHEI!')
    print('Tente novamente.')
