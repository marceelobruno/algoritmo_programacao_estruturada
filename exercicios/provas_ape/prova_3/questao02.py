def forma_triangulo(a, b, c):
    triangulo = False
    if (a < b + c) and (b < a + c) and (c < a + b):
        triangulo = True
    else:
        triangulo = False
    return triangulo


def tipo_triangulo(a, b, c, forma_triangulo):
    if forma_triangulo:
        if (a == b) and (a == c):
            return 'Equilátero'
        elif (a == b) and (a != c):
            return 'Isósceles'
        elif (a != b) and (a != c):
            return 'Escaleno'


print('Informe 3 lados do triangulo:')
n1 = int(input())
n2 = int(input())
n3 = int(input())
triangulo = forma_triangulo(n1, n2, n3)

print(f'Os lados:\nA: {n1}\nB: {n2}\nC: {n3}')
if forma_triangulo(n1, n2, n3,):
    print(f'Formam um triângulo do tipo: {tipo_triangulo(n1, n2, n3, forma_triangulo(n1, n2, n3))}')
else:
    print('Não formam um triângulo.')
