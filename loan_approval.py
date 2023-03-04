casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
tempo = int(input('Em quantos anos você quer pagar: '))
valor_mensal_casa = casa / (tempo * 12)
porcentagem_do_salário = salario / 100 * 30
if valor_mensal_casa > porcentagem_do_salário:
    print('Empréstimo negado, o valor mensal da casa irá ultrapassar os 30 por cento do seu salário!')
    print(f'O valor mensal da casa é {valor_mensal_casa:.2f} e poderia ser no máximo {porcentagem_do_salário:.2f}!')
elif valor_mensal_casa < porcentagem_do_salário:
    print('Empréstimo aprovado, você poderá comprar a casa!')
    print(f'O valor mensal da casa será de {valor_mensal_casa:.2f}')
