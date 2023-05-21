# Solicitar N números do usuário (até que o usuário digite o número zero)
# e a cada leitura mostrar o dobro desse número.

iterador = 1
qtd = int(input('Digite a quantidade de iterações: '))

while iterador <= qtd:
    numero = int(input('Digite outro número inteiro: '))
    if numero == 0:
        print('\nO programa parou, pois você informou o número 0.')
        break
    print(f'O dobro de {numero} é {numero*2}.')
    iterador += 1
