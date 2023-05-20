var_a = int(input('Informe um valor inteiro: '))
var_b = int(input('Informe outro valor inteiro: '))

print(f'Valor inicial das variáveis A: {var_a} e B: {var_b}')

var_c = var_a
var_a = var_b
var_b = var_c

print(f'Valor final das variáveis A: {var_a} e B: {var_b}')
