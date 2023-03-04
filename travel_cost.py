distancia_viagem = int(input('Distância da viagem: '))
if distancia_viagem <= 200:
    valor = distancia_viagem * 0.50
    print(f'O custo da viagem de {distancia_viagem}km será de R${valor}!')
else:
    valor = distancia_viagem * 0.45
    print(f'O custo da viagem de {distancia_viagem}km será de R${valor}!')