"""
Uma certa empresa pretende verificar se os seus empregados estarão qualificados ou não para aposentadoria em 2022. 
Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
* Ter no mínimo 65 anos de idade; ou
* Ter trabalhado no mínimo 30 anos; ou
* Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.

Com base nas informações acima, faça um programa para:
* Ler o nome do empregado, o ano de nascimento e o ano de seu ingresso na empresa. 
* Calcular e exibir a idade e o tempo de trabalho do empregado (estimado ao final de 2021) 
* Exibir a mensagem “Pode Requerer Aposentadoria” se atender aos requisitos ou “Não Pode Requerer Aposentadoria” caso contrário.

Ao final de cada execução, o programa deverá perguntar se o usuário deseja fazer nova verificação. Se sim, o programa deverá repetir tudo novamente, caso contrário deverá encerrar.
"""
while True:
    nome = input('Informe o seu nome: ').title()
    ano_nasc = int(input('Informe o ano em que nasceu: '))
    ano_ingresso = int(input('Informe o ano de ingresso na empresa: '))

    idade = 2021 - ano_nasc
    tempo_sev = 2021 - ano_ingresso

    print(f'\nIdade: {idade} anos')
    print(f'Tempo de trabalho: {tempo_sev} anos')

    if (idade>=65) or (tempo_sev>=30) or (idade>=60 and tempo_sev>=25):
        print('Pode requerer aposentadoria')
    else:
        print('Não pode requerer aposentadoria')

    if input('\nDeseja fazer nova verificação (s/n)? ').lower() == 'n':
        break
    print()
