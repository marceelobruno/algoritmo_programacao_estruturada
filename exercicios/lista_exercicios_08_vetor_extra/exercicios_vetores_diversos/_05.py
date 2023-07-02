"""
http://www.ic.uff.br/~ccaetano/aulas/lista-vetores-matrizes.pdf

5. Faça um programa que leia e monte dois vetores de números 
inteiros com 20 números cada. 
Depois de montados gere um terceiro vetor formado pela diferença dos dois
vetores lidos, um quarto vetor formado pela soma dos dois vetores lidos
e por último um quinto vetor formado pela multiplicação dos dois vetores lidos.
Imprima todos os vetores.
"""
from random import randint

tam = 20

# criação dos vetores
vet_a = []
vet_b = []
vet_c = []
vet_d = []
vet_e = []

# preenchendo vetores principais
for i in range(tam):
    num = randint(1, 30)
    vet_a.append(num)
    num2 = randint(1, 30)
    vet_b.append(num2)

# preenchendo vetores auxiliares
for i in range(tam):
    vet_c.append(vet_a[i] - vet_b[i])
    vet_d.append(vet_a[i] + vet_b[i])
    vet_e.append(vet_a[i] * vet_b[i])

# imprimindo vetores
print(f'''
Vetor A: {vet_a}
Vetor B: {vet_b}
Vetor C - Diferença: {vet_c}
Vetor D - Soma: {vet_d}
Vetor E - Multiplicação: {vet_e}''')
