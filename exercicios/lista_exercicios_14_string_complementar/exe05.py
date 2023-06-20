"""
5. Faça um programa que leia uma frase e a exiba na tela conforme o exemplo abaixo.
Entrada: ABCDE
Saída:  A
        BB
        CCC
        DDDD
        EEEEEE
        DDDD
        CCC
        BB
        A
"""
frase = input('Frase: ').upper()
n = len(frase)

for i in range(n):
    print(frase[i]*(i+1))

for i  in range(n-2,-1,-1):
    print(frase[i]*(i+1))
