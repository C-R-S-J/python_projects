ano = int(input('Digite qual ano quer analisar para saber se é bissexto: '))
resultado = ano % 4
if resultado == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')