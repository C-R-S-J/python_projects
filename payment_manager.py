compra = float(input('Digite o valor da compra: '))
escolha = int(input('''Formas de pagamento
[ 1 ] Cartão de crédito
[ 2 ] Cartão de crédito 2x
[ 3 ] Cartão de crédito 3x ou mais
[ 4 ] Cartão de débito
[ 5 ] Dinheiro
Opção: '''))
if escolha == 1:
    valor = compra * 0.05
    valor_final = compra - valor
    print(f'O valor da compra que era de R${compra:.2f} passará para R${valor_final:.2f}!')
elif escolha == 2:
    print(f'O valor não sofrerá alterações e será cobrado R${compra:.2f}')
elif escolha == 3:
    parcelas = int(input('Quantas parcelas: '))
    valor_final = (compra * 0.20) + compra
    parcela_total = valor_final / parcelas
    print(f'A compra no valor de R${compra:.2f} terá um acréscimo de 20%, resultando no valor de R${valor_final:.2f} com parcelas de R${parcela_total:.2f}!')
elif escolha == 4 or 5:
    valor_final = compra - (compra * 0.05)
    print(f'A compra no valor de {compra:.2f} terá um desconto 5%, resultado no valor de R${valor_final:.2f}')