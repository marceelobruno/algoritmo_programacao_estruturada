"""
16. Faça um programa que leia um vetor de 5 posições para números reais e, depois,
um código inteiro. Se o código for zero, finalize o programa; se for 1, mostre
o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa.
Caso o código for diferente de 1 e 2 escreva uma mensagem informando que o código é inválido.
"""
n = 5
vet = [None] * n
vet_inv = [None] * n

print(f'Informe {n} valores:')
for i in range(n):
    vet[i] = int(input())
    for j in range(n):
        vet_inv[n - 1 - j] = vet[j]
        continue

cod = int(input('Informe um valor inteiro para o código: '))

if cod == 0:
    print('Fim do programa!')
elif cod == 1:
    print('Vetor original: ', vet)
elif cod == 2:
    print('Vetor invertido: ', vet_inv)
elif cod not in (1, 2):
    print('Código inválido!')
