numero = int(input('Digite um número: '))
numero_dois = int(input('Digite outro número: '))
if numero > numero_dois:
    print(f'O maior número é {numero} e o menor é {numero_dois}!')
elif numero_dois > numero:
    print(f'O maior número é {numero_dois} e o menor é {numero}!')
else:
    print('Os dois são iguais!')