peso = int(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

print('Grau de obesidade: ', end='')
if imc >= 30:
    print('Obesidade.')
elif imc >= 18.5 and imc < 25:
    print('Normal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
else:
    print('Baixo peso.')
