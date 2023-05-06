quantidade = int(input('Informe quantos números: '))

somatorio = 0

for i in range(quantidade):
    valor = int(input(f'Digite o {i + 1}° valor: '))
    somatorio += valor

print(f'O somatório foi: {somatorio}')
