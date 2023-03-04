salario_inicial = float(input('Qual o salário do funcionário: '))
if salario_inicial <= 1250.00:
    salario_porcentagem = salario_inicial * 15 / 100
    salario_final = salario_porcentagem + salario_inicial 
    print(f'O salário final vai ser de R${salario_final:.2f} com o reajuste de 15%!')
else:
    salario_porcentagem = salario_inicial * 10 / 100
    salario_final = salario_porcentagem + salario_inicial
    print(f'O salário final vai ser de R${salario_final:.2f} com o reajuste de 10%!')
