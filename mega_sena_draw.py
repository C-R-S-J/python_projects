from random import randint
from time import sleep
jogo = list()
lista = list()
print('='*32)
print('SORTEADOR DE JOGOS DA MEGA SENA' )
print('='*32)
quantidade = int(input('Quantos jogos você quer que eu sorteie: '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total +=1
for i, l in enumerate(jogo):
    print(f'Jogo {i+1} : {l}')
    sleep(2)
print('Boa sorte nos próximos jogos')