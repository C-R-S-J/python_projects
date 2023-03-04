n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'O maior número é o {n1}!')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é o {n2}!')
elif n3 > n1 and n3 > n2:
    print(f'O maior número é o {n3}!')
#verificação de menor número
if n1 < n2 and n1 < n3 :
    print(f'O menor número é {n1}!')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}!')
elif n3 < n1 and n3 < n2:
    print(f'O menor número é {n3}!')