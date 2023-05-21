# Solicitar N números do usuário e ao final da leitura mostrar a soma de todos os números lidos.

soma = 0
num = int(input('Quantidade de iterações: '))

for n in range(num):
    valor = int(input('Informe um outro número inteiro: '))
    soma += valor

print(f'A soma dos números informados é {soma}.')
