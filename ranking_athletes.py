from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos!')
if idade <= 9:
    print('O atleta é categoria MIRIM!')
elif idade > 9 and idade <= 14:
    print('O atleta é categoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print('O atleta é categoria JUNIOR!')
elif idade > 19 and idade <= 25:
    print('O atleta é categoria SÊNIOR!')
else:
    ('O atleta é categoria MASTER!')