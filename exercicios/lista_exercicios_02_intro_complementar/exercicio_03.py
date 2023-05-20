""" 3 - Escreva um programa que leia duas variáveis inteiras e troque o conteúdo
entre elas, mostrando o resultado."""

variavel_a = int(input('Informe um valor inteiro para a primeira variável: '))
variavel_b = int(input('Informe um valor inteiro para a segunda variável: '))

variavel_c = variavel_a
variavel_a = variavel_b
variavel_b = variavel_c

print(f'Os valores das variáveis foram trocados. Agora a primeria variável \
vale {variavel_a} e a segunda variável vale {variavel_b}.')
