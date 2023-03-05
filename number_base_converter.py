num = int(input('Digite um número: '))
print('''Qual conversão você quer usar: 
    [ 1 ] converter para binário
    [ 2 ] converter para octal
    [ 3 ] converter para hexadecimal''')
opção = int(input('Opção: '))
if opção == 1:
    print(f'{num} convertido para binário fica {bin(num)}')
elif opção == 2:
    print(f'{num} convetido para octal fica {oct(num)}')
elif opção == 3:
    print(f'{num} convertido para hexadecimal fica {hex(num)}')
else:
    print('Opção invalida!')