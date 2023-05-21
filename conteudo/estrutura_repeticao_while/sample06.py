"""
Solicitar N números do usuário (até que o usuário digite o número zero ou a soma dos
números lidos seja maior do que 100) e ao final da leitura mostrar a soma de todos os
números lidos.
"""
iterador = 1
soma = 0
quantidade = int(input('Qual a quantidade de iterações: '))

while iterador <= quantidade:
    print('Digite outro número inteiro: ',end="")
    numero = int(input())
    if (numero == 0 or numero > 100) or soma > 100:
        print('Você digitou o número 0 ou atingiu o limite de 100 números informados')
        break
    soma+=numero
    iterador+=1
print(f'A soma de todos os números informados foi: {soma}')
