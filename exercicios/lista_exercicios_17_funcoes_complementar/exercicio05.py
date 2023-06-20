def fatorial(valor):
    fat = 1
    for i in range(2, valor + 1):
        fat *= i
    return fat


def potencia(base, expoente):
    return base ** expoente


def cosseno(x):
    cos = 1
    sinal = -1
    for i in range(2, 40, 2):
        cos += sinal * potencia(x, i) / fatorial(i)
    sinal *= -1
    return cos
