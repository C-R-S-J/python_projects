numero_um = int(input('Digite o primeiro número: '))
numero_dois = int(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    escolha = int(input('Qual a sua opção: '))
    if escolha == 1:
        soma = numero_um + numero_dois
        print(f'A soma de {numero_um} e {numero_dois} é {soma}!')
        escolha = int(input('o que você quer fazer agora: '))
    elif escolha == 2:
        multiplicação = numero_um * numero_dois
        print(f'A multiplicação entre {numero_um} e {numero_dois} é {multiplicação}')
        escolha = int(input('O que você quer fazer agora: '))
    elif escolha == 3:
        if numero_um > numero_dois:
            print(f'O maior número é {numero_um}!')
            escolha = int(input('O que você quer fazer agora: '))
        else:
            print(f'O maior número é {numero_dois}!')
            escolha = int(input('O que você quer fazer agora: '))
    elif escolha == 4:
        numero_um = int(input('Digite o primeiro número: '))
        numero_dois = int(input('Digite o segundo número: '))
    else:
        print('Opção inválida!')
print('Fim do programa')
    