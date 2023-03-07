for c in range (3):
    n = int(input('Digite um número: '))
    if n % 2:
        n += 1
    else:
        n += 0
print(f'A soma dos valores pares é {n}.')