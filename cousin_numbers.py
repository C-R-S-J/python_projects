num = int(input('Digite um número: '))
contadores = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        contadores += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}',end = '')
print(f'\n\033[mO número {num} foi divisível {contadores} vezes' )
if contadores == 2:
    print('É um número primo')
else:
    print('Não é um número primo')