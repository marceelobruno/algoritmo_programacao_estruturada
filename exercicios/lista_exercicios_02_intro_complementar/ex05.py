tempo_em_segundos = int(input('Informe o tempo desejado em segundos: '))

hora = tempo_em_segundos // 3600

resto = tempo_em_segundos % 3600

minuto = resto // 60

segundo = resto % 60

print(f'Resultado: {hora}h, {minuto}min, {segundo}s.')
