from random import randint
palpites = 1
print('*'*30)
print('JOGO DE ADIVINHAÇÃO VERSÃO 2.0')
print('*'*30)
print('Acabei de escolher um número entre 1 e 10.')
print('Tente adivinhar se puder!')
escolhido_computador = randint(1,10)
escolha_jogador = int(input('Digite o palpite: '))
while escolha_jogador != escolhido_computador:
    if escolha_jogador < escolhido_computador :
        print('Você errou, pensei em um valor maior!')
        escolha_jogador = int(input('Tente novamente: '))
        palpites += 1
    else:
        print('Você errou, pensei num valor menor!')
        escolha_jogador = int(input('Tente novamente: '))
        palpites += 1
print(f'Você acertou parabéns, precisou de {palpites} tentativas! ')
