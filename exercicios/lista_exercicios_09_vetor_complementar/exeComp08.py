# ruff: noqa: E501

"""
Dadas as temperaturas que foram registradas diariamente durante uma semana,
deseja-se determinar em quantos dias dessa semana a temperatura esteve acima da média.
Escreva um programa (utilizando vetores) para calcular esta informação.
"""
dias = 7
semana = [None] * dias
cont = 0

for i in range(dias):
    print(f'Informe a temperatura do {i+1}° dia: ')
    semana[i] = int(input())

soma = sum(semana)
media = soma / dias

print(f'Temperatura média {media:.2f}')

for i in range(dias):
    if semana[i] > media:
        cont += 1

if cont > 0:
    print(f'Houve {cont} dia(s) acima da temperatura média.')
else:
    print('Não houve nenhum dia acima da média.')
