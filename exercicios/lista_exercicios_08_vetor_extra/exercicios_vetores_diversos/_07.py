"""
https://www.ime.usp.br/~macmulti/exercicios/vetores/index.html

7. Dada uma seqüência de n números reais, determinar os números que compõem
a seqüência e o número de vezes que cada um deles ocorre na mesma.

Exemplo: n = 8
Seqüência: -1.7, 3.0, 0.0, 1.5, 0.0, -1.7, 2.3, -1,7
Saída: -1.7 ocorre 3 vezes
        3.0 ocorre 1 vez
        0.0 ocorre 2 vezes
        1.5 ocorre 1 vez
        2.3 ocorre 1 vez
"""
n = 8
vet = []
repetido = []
# preenchendo o vetor
for i in range(n):
    num = float(input(f'Digite o {i+1}° número: '))
    vet.append(num)
print()

# contando as ocorrências
for i in range(n):
    if vet.count(vet[i]) > 1:
        if vet[i] in repetido:
            continue
        else:
            print(f'{vet[i]} ocorre {vet.count(vet[i])} vezes')
            repetido.append(vet[i])
    else:
        print(f'{vet[i]} ocorre {vet.count(vet[i])} vez')
