"""
https://wiki.python.org.br/ExerciciosListas

15. Faça um programa que leia um número indeterminado de valores, correspondentes
as notas, encerrando a entrada de dados quando for informado um valor igual a -1
(que não deve ser armazenado). Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem; 
"""
notas = []

print('Informe algumas notas:')
while True:
    num = int(input('Nota: '))
    if num == -1:
        break
    notas.append(num)

while True:
    opcoes = 'abcdefgh'

    print('''
    Menu
    a. Mostre a quantidade de valores que foram lidos;
    b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d. Calcule e mostre a soma dos valores;
    e. Calcule e mostre a média dos valores;
    f. Calcule e mostre a quantidade de valores acima da média calculada;
    g. Calcule e mostre a quantidade de valores abaixo de sete;
    h. Encerre o programa com uma mensagem;''')

    opcao = input('\nDigite sua opção: ').lower()

    match opcao:
        case 'a':
            print('Quantidade de valores armazenados:', len(notas))
        case 'b':
            print('Vetor:', notas)
        case 'c':
            for i in range(len(notas)):
                print(notas[len(notas) - 1 - i])
        case 'd':
            print('Soma das notas:', sum(notas))
        case 'e':
            print('Média dos valores informados:', sum(notas) / len(notas))
        case 'f':
            media = sum(notas) / len(notas)
            cont = 0
            for i in notas:
                if i > media:
                    cont += 1
            print('Quantidade de valores acima da média:', {cont})
        case 'g':
            cont = 0
            for i in notas:
                if i < 7:
                    cont += 1
            print('Quantidade de valores abaixo de 7:', {cont})
        case 'h':
            print('Fim do programa!')
            break
