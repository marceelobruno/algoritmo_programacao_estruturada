data = input('Data: ').split('/')
cliente = input('Cliente: ').title().split()
brinquedo = input('Brinquedo: ').upper()

print(f'{cliente[0][0]}{cliente[-1]}_{brinquedo}_{data[-1]}{data[1]}{data[0]}')
