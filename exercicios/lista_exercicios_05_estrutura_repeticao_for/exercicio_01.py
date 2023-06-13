"""
1 - Faça um programa que calcule e mostre os números múltiplos de 5 do
intervalo 50 a 300, juntamente com suas raízes e seus cubos.
"""
import math

contador = 0

for i in range(50, 301, 5):
    raiz = math.sqrt(i)
    print(f'{i}: Sua raíz é {raiz:.2f} e o cubo é: {i ** 3}.')
    contador += 1

print(f'Foram gerados {contador} múltiplos de 5.')
