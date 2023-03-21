s = 0
while True:
    n = (int(input('Digite um número [Digite 999 para parar]: ')))
    if n != 999:
        s += n
    else:
        break
print(f'A soma dos valores digitados foi {s}')