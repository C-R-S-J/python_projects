num = cont = som = 0
num = int(input('Digite um número [Digite 999 para parar]: '))
while num != 999:
    som += num
    cont += 1
    num = int(input('Digite um número [Digite 999 para parar]: '))
print(f'Você digitou {cont} e a soma entre eles foi {som}!')

