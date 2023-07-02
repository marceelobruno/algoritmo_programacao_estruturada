"""
https://www.facom.ufu.br/~backes/gsi002/ListaC04.pdf

Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor.
Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos, sendo
que caso o usuário digite um número que já foi digitado anteriormente, o programa
deverá pedir para ele digitar outro número. Note que cada valor digitado pelo
usuário deve ser pesquisado no vetor, verificando se ele existe entre os números
que já foram fornecidos. Exibir na tela o vetor final que foi digitado.
"""
tam = 10
cont = 0
vet = []

while True:
    num = int(input('\nInforme um número: '))
    if num in vet:
        print('Número repetido! Informe outro número.')
    else:
        vet.append(num)
        cont += 1
    if cont == tam:
        break

print('\nValores informados ao vetor:', vet)
