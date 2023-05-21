"""
Faça um programa que solicite do usuário uma palavra.
• Se a palavra informada for igual a “fim” o programa deverá exibir “Digitou fim - Palavra
Certa!!!” e parar a sua execução.
• Caso contrário, o programa deverá exibir “Palavra Errada! Digite nova palavra” e uma nova
palavra deverá ser solicitada ao usuário.
"""

PALAVRA_CERTA = 'fim'

palpite = input('Advinhe qual é a palavra secreta: ')
while PALAVRA_CERTA != palpite:
    print("Palavra Errada! Digite nova palavra")
    palpite = input('Advinhe qual é a palavra secreta: ')
else:
    print("Digitou fim - Palavra Certa!!!")
