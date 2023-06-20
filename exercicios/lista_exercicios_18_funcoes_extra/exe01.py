"""
https://www.facom.ufu.br/~backes/gsi002/ListaC07.pdf
Receber uma data no formato DD/MM/AAAA e retornar a data formatada. Exemplo:
Entrada: 22/09/1999
Saída: 22 de Set de 1999
"""


def saber_mes(num: str) -> str:
    meses = ['Jan', 'Fev', 'Mar', 'Abr',
             'Mai', 'Jun', 'Jul', 'Ago',
             'Set', 'Out', 'Nov', 'Dez']
    i = int(num) - 1
    return meses[i]


# Testando a função
data = input('Informe uma data DD/MM/AAAA: ').split('/')

print(f'{data[0]} de {saber_mes(data[1])} de {data[-1]}')
