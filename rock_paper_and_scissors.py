import random

pontuacao_jogador = 0
pontuacao_computador = 0

while True:
    escolha_jogador = input("Escolha pedra, papel ou tesoura: ")
    escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])
    print("O computador escolheu:", escolha_computador)

    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
            (escolha_jogador == 'papel' and escolha_computador == 'pedra') or \
            (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
        print("Você ganhou essa rodada!")
        pontuacao_jogador += 1
    else:
        print("O computador ganhou essa rodada!")
        pontuacao_computador += 1

    print("Pontuação atual: Jogador:", pontuacao_jogador, "Computador:", pontuacao_computador)

    jogar_novamente = input("Deseja jogar novamente? (s/n) ")
    if jogar_novamente.lower() != 's':
        break
