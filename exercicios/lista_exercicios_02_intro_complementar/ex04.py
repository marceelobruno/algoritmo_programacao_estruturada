hodometro_inicial = int(input('Informe o hodômetro de início da viagem: '))

hodometro_final = int(input('Informe o hodômetro final da viagem: '))

combustivel_gasto = float(input('Quantos litros de combustível foram gastos na viagem: '))

preco_combustivel = float(input('Qual o preço do litro de combustível: R$ '))

capacidade_tanque = int(input('Informe a capacidade do tanque de combustível do veículo: '))

quilometros_rodados = hodometro_final - hodometro_inicial

km_por_litro = quilometros_rodados / combustivel_gasto

autonomia_veiculo = capacidade_tanque * km_por_litro

custo_viagem = combustivel_gasto * preco_combustivel

print(
    f'Olá, Motorista! Você rodou {quilometros_rodados}km, seu veículo fez {km_por_litro:.1f}km/l e possui uma autonomia de {autonomia_veiculo:.0f}km, e ao fim da viagem, você gastou R${custo_viagem:.2f}.')
