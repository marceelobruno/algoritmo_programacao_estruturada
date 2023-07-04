"""
https://www.facom.ufu.br/~backes/gsi002/ListaC04.pdf

15. Leia um vetor de 10 posições.
Escreva os elementos do vetor eliminando elementos repetidos.
"""
tam = 5
vet = []

cont = 0
print('Preencha o vetor:')
while True:

    if cont == tam:
        break
    num = int(input('Elemento: '))
    if num in vet:
        print('Número já informado. Tente novamente!')
        continue
    else:
        vet.append(num)
        cont += 1

print('\nVetor:', vet)
