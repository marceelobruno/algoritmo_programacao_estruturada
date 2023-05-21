"""
5 - Escreva um programa para determinar as raízes de uma equação de segundo grau,
dados os seus coeficientes e usando a fórmula de Bhaskara (Equação Quadrática).
x = (-b ± √(b² - 4ac)) / (2a)
OBS: se o delta for negativo, não existem as raízes da equação.
Dica: use a função sqrt do módulo math.
"""
import math

print('Digite os coeficientes da Equação de 2º grau: ')
a = float(input())
b = float(input())
c = float(input())

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print('Não há raízes.')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f'As raízes da equação são {x1:.1f} e {x2:.1f}')
