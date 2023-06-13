"""
Faça um programa que solicite ao usuário uma senha. Caso a senha digitada
esteja correta, o programa deverá mostrar senha correta. Caso contrário, o
programa deverá mostrar senha incorreta e pedir para o usuário tentar
novamente digitar a senha correta. Mas, se o usuário fornecer três senhas
incorretas, o programa deverá encerrar a sua execução.
Obs: a senha correta é “abcd”
"""

PALAVRA = 'abcd'
tentativa = 0

while tentativa < 3:
    senha = input('Digite a senha: ')
    if senha == PALAVRA:
        print(f'Você acertou! "{PALAVRA}" é a senha correta.')
        break
    else:
        print('Não foi dessa vez! Tente novamente.')
    tentativa+=1
