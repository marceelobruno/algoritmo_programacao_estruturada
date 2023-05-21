# Solicitar N números do usuário e a cada leitura mostrar o dobro desse número

iterador = 0
num = int(input('Informe uma determinada quantidade de números: '))

for n in range(num):
    n = int(input('Insira um número inteiro: '))
    print(f'O dobro de {n} é {n*2}.')
    iterador += n
