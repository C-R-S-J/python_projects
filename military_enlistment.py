from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
if idade == 18:
    print('Você deve se alistar esse ano.')
elif idade < 18:
    falta = 18 - idade
    print(f'Ainda não é seu ano de alistamento, falta {falta} anos.')
elif idade > 18:
    atraso = idade - 18
    print(f'Você já deveria ter alistado a {atraso} anos!')