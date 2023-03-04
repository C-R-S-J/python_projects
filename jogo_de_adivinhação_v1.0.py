from random import randint
numero_escolhido_comp = randint(1,5)
escolha_jogador = int(input('Tente adivinhar que número estou pensando de 1 a 5: '))
if escolha_jogador == numero_escolhido_comp :
    print('Você acertou, parabéns!')
else:
    print(f'Você errou, eu pensei no {numero_escolhido_comp}')
    