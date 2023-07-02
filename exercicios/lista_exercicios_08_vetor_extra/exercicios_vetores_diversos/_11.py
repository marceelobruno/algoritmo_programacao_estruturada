"""
http://www.decom.ufop.br/romildo/2019-2/bcc702/Aula6-Exercicios-Vet-Mat.pdf

09. Escreva um programa que receba como entrada uma frase e uma letra, e
calcule o percentual que indica a quantidade de ocorrências dessa letra com
relação ao total de caracteres válidos (letras). 
Não considere o espaço como um caractere válido.
Exiba a resposta com duas casas decimais.
"""
frase = input('Digite uma frase: ').lower()
letra = input('Digite uma letra: ').lower()
vet_frase = []

for i in range(len(frase)):
    if frase[i] == ' ':
        continue
    else:
        vet_frase.append(frase[i])

tamanho = len(vet_frase)
contagem = vet_frase.count(letra)

percent = (contagem / tamanho) * 100

print(f'A letra {letra} ocorre {percent:.2f}% vez(es) na frase: {frase}')
