numero = [[],[]]
valor = 0
for c in range (1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
numero[0].sort()
numero[1].sort()
print('*'*20)
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Todos os valores digitados ímpares: {numero[1]}')