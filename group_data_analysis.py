maiores = homens = mulheres_menor = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maiores +=1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade < 20:
        mulheres_menor +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos são {maiores}')
print(f'Ao todo temos {homens} cadastrados')
print(f'E temos {mulheres_menor} mulheres com menos de 20 anos cadastradas.')