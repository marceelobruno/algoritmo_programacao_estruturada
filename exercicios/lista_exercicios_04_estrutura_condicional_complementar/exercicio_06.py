"""
6 - Na primeira etapa de um concurso, o candidato tem que fazer duas provas.
Dessas duas notas é tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a segunda etapa do concurso. Na segunda etapa, ele fará mais
uma prova, onde deverá obter uma nota maior ou igual a 8.0 para ser aprovado no concurso.
Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa,e se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga
se ele foi aprovado ou não no concurso.
"""

print('1ª Etapa')
primeira_nota = float(input('Informe sua 1ª nota: '))
segunda_nota = float(input('Informe sua 2ª nota: '))

media = (primeira_nota + segunda_nota) / 2

if media >= 7.0:
    print('Apto para a 2ª Etapa')
    terceira_nota = float(input('Informe sua 3ª nota: '))
    if terceira_nota >= 8.0:
        print('Candidato Aprovado!')
    else:
        print('Candidato Reprovado!')
else:
    print('Candidato Eliminado na 1ª etapa')
