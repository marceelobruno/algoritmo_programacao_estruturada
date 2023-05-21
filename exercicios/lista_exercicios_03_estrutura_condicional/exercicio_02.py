"""Escreva um programa que leia dois números e exiba-os em ordem crescente."""

# num_1 = int(input('Informe um número: '))
# num_2 = int(input('Informe outro número: '))

# if num_1 < num_2:
#     print(f'Esta é a ordem crescente dos números informados: {num_1}, {num_2}')

# else:
#     print(f'Esta é a ordem crescente dos números informados: {num_2}, {num_1}')

print('Digite dois números inteiros:')
a = int(input())
b = int(input())

print('Números em ordem crescente: ',end='')
if a < b:
    print(a,b)
else:
    print(b,a)
