"""
3. Ler um conjunto de números reais, armazenando-o em vetor e calcular o 
quadrado dos componentes deste vetor, armazenando o resultado em outro vetor.
OBS: Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""
tam = 5
a = [0]*tam
b = [0]*tam

print(f'Informe {tam} elementos: ')
for i in range(tam):
    print(f'Digite o {i+1} valor: ',end=' ')
    num = float(input())
    a[i] = num
    b[i] = num ** 2

print('Valores do conjunto A: ',a)
print('Valores do conjunto B: ',b)
