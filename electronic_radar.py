velocidade_do_carro = int(input('Velocidade do carro: '))
if velocidade_do_carro > 80 :
    multa = velocidade_do_carro - 80
    multa_valor = multa * 7
    print(f'Você passou do limite de velocidade, multa gerada no valor de {multa_valor}')
else :
    print('Velocidade não ultrapassada.')