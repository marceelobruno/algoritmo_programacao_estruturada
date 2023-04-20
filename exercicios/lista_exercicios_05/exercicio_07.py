numero = int(input('Digite um valor para saber se o número é primo: '))

if numero <= 1:
    eh_primo = False
else:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break
if eh_primo:
    print(f'{numero} é primo!')
else:
    print(f'{numero} não é primo!')
