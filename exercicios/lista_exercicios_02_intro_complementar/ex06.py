bits_desejados = int(input('Informe a quantidade de bits desejados para o saque: B$'))

cinquenta = bits_desejados // 50
resto = bits_desejados % 50
dez = resto // 10
resto_2 = resto % 10
cinco = resto_2 // 5
dois = resto_2 % 5

print(
    f'Para B${bits_desejados} seriam as seguintes notas:  \
    \n- {cinquenta} nota(s) de B$50 \n- {dez} nota(s) de B$10 \
    \n- {cinco} nota(s) de B$5 \n- {dois} nota(s) de B$1')
